#!/usr/bin/env python3
"""
GIT_SEQUENCE_EDITOR script for mu_basecore rebase onto edk2-stable202602.
Processes the interactive rebase todo file:
  1. Drops cherry-picks already in edk2-stable202602
  2. Drops revert pairs
  3. Squashes [SQUASH ON REBASE] commits with their targets
"""

import sys
import os
import re

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def load_drops():
    """Load the set of commit hashes (12-char) to drop."""
    drops = set()
    path = os.path.join(SCRIPT_DIR, "rebase_drops.txt")
    with open(path) as f:
        for line in f:
            h = line.strip()
            if h:
                drops.add(h)
    return drops

def load_squashes():
    """Load squash operations as list of (squash_hash, target_hash)."""
    squashes = []
    path = os.path.join(SCRIPT_DIR, "rebase_squashes.txt")
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split("|")
            squashes.append((parts[0], parts[1]))
    return squashes

def parse_todo_line(line):
    """Parse a todo line into (action, hash, rest) or None if not a pick line."""
    line = line.rstrip("\n")
    m = re.match(r'^(pick|drop|squash|fixup|edit|reword|exec|break)\s+([a-f0-9]+)\s+(.*)', line)
    if m:
        return m.group(1), m.group(2), m.group(3)
    return None

def process_todo(todo_path):
    with open(todo_path) as f:
        lines = f.readlines()

    drops = load_drops()
    squashes = load_squashes()

    # Additional manual squash: 5e381f8de665 also squashes with fb5e75cbf1c4
    # (the original script only captured one of two targets)
    # Add fb5e75cbf1c4 as a squash into b8960d8a908c as well
    squashes.append(("fb5e75cbf1c4", "b8960d8a908c"))

    # d5a9eeef9fe6 squashes with 77849807d223
    squashes.append(("d5a9eeef9fe6", "77849807d223"))

    # Build lookup: hash_prefix -> line_index for todo entries
    todo_entries = []  # List of (action, hash, subject, original_line_index)
    comment_lines = []  # Lines that are comments or blank

    for i, line in enumerate(lines):
        parsed = parse_todo_line(line)
        if parsed:
            action, hash_val, subject = parsed
            todo_entries.append([action, hash_val, subject, i])
        else:
            comment_lines.append((i, line))

    # Step 1: Mark drops
    for entry in todo_entries:
        for drop_hash in drops:
            if entry[1].startswith(drop_hash[:10]) or drop_hash.startswith(entry[1][:10]):
                entry[0] = "drop"
                break

    # Step 2: Process squashes
    # Build a hash->index map for the entries
    def find_entry_index(hash_prefix):
        for idx, entry in enumerate(todo_entries):
            if entry[1].startswith(hash_prefix[:10]) or hash_prefix.startswith(entry[1][:10]):
                return idx
        return None

    # Collect squash moves: (squash_entry_index, target_entry_index)
    squash_moves = []
    for squash_hash, target_hash in squashes:
        sq_idx = find_entry_index(squash_hash)
        tgt_idx = find_entry_index(target_hash)

        if sq_idx is None:
            print(f"WARNING: squash commit {squash_hash} not found in todo", file=sys.stderr)
            continue
        if tgt_idx is None:
            print(f"WARNING: squash target {target_hash} not found in todo, keeping as pick", file=sys.stderr)
            continue
        if todo_entries[sq_idx][0] == "drop":
            # Already being dropped (e.g., cherry-pick that's also squash-on-rebase)
            continue

        squash_moves.append((sq_idx, tgt_idx))

    # Apply squash moves: remove squash entries, insert after targets
    # Sort by squash index descending to avoid index shifting issues
    # Group squashes by target
    target_groups = {}
    for sq_idx, tgt_idx in squash_moves:
        if tgt_idx not in target_groups:
            target_groups[tgt_idx] = []
        target_groups[tgt_idx].append(sq_idx)

    # Remove squash entries from their current positions and mark for reinsertion
    entries_to_move = {}  # target_idx -> [entries]
    indices_to_remove = set()
    for tgt_idx, sq_indices in target_groups.items():
        entries_to_move[tgt_idx] = []
        for sq_idx in sorted(sq_indices):
            entry = todo_entries[sq_idx]
            entry[0] = "squash"
            entries_to_move[tgt_idx].append(entry)
            indices_to_remove.add(sq_idx)

    # Rebuild the todo list
    new_entries = []
    for i, entry in enumerate(todo_entries):
        if i in indices_to_remove:
            continue
        new_entries.append(entry)
        # Insert squash entries after this target
        if i in entries_to_move:
            for sq_entry in entries_to_move[i]:
                new_entries.append(sq_entry)

    # Write back
    with open(todo_path, "w") as f:
        for entry in new_entries:
            f.write(f"{entry[0]} {entry[1]} {entry[2]}\n")
        # Append comment lines
        for _, line in comment_lines:
            f.write(line)

    # Stats
    dropped = sum(1 for e in new_entries if e[0] == "drop")
    squashed = sum(1 for e in new_entries if e[0] == "squash")
    picked = sum(1 for e in new_entries if e[0] == "pick")
    print(f"Todo processed: {picked} pick, {squashed} squash, {dropped} drop", file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <todo-file>", file=sys.stderr)
        sys.exit(1)
    process_todo(sys.argv[1])
