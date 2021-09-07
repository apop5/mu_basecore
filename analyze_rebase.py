#!/usr/bin/env python3
"""
Rebase todo processor for mu_basecore onto edk2-stable202602.
Analyzes commits and generates a GIT_SEQUENCE_EDITOR script.
"""

import subprocess
import re
import sys
import os

TARGET_TAG = "edk2-stable202602"
BASE_TAG = "edk2-stable202511"
RELEASE_BRANCH = "release/202511"

def run_git(args):
    result = subprocess.run(["git"] + args, capture_output=True, text=True, cwd=r"Q:\code\mu_basecore")
    return result.stdout.strip(), result.returncode

def get_commit_message(hash):
    out, _ = run_git(["log", "-1", "--format=%B", hash])
    return out

def get_commit_subject(hash):
    out, _ = run_git(["log", "-1", "--format=%s", hash])
    return out

def is_ancestor(commit, target):
    _, rc = run_git(["merge-base", "--is-ancestor", commit, target])
    return rc == 0

def get_all_commits():
    """Get all commits in the rebase range as (short_hash, full_hash, subject)"""
    out, _ = run_git(["log", "--format=%H %s", f"{BASE_TAG}..{RELEASE_BRANCH}"])
    commits = []
    for line in out.splitlines():
        if not line.strip():
            continue
        parts = line.split(" ", 1)
        full_hash = parts[0]
        subject = parts[1] if len(parts) > 1 else ""
        commits.append((full_hash[:12], full_hash, subject))
    return commits

def analyze_cherry_picks(commits):
    """Returns set of full hashes to drop (cherry-picks whose source is in target tag)"""
    drops = set()
    keeps = set()
    cherry_pick_pattern = re.compile(r'\[Cherry-Pick\]|\[CHERRY-PICK\]', re.IGNORECASE)
    source_pattern = re.compile(r'cherry picked from commit ([a-f0-9]+)')

    for short, full, subject in commits:
        if not cherry_pick_pattern.search(subject):
            continue

        msg = get_commit_message(full)
        m = source_pattern.search(msg)
        if m:
            source_hash = m.group(1)
            if is_ancestor(source_hash, TARGET_TAG):
                drops.add(full)
                print(f"  DROP cherry-pick {short} -> source {source_hash[:12]} is in {TARGET_TAG}")
            else:
                keeps.add(full)
                print(f"  KEEP cherry-pick {short} -> source {source_hash[:12]} NOT in {TARGET_TAG}")
        else:
            keeps.add(full)
            print(f"  KEEP cherry-pick {short} -> no source hash found")

    return drops

def analyze_reverts(commits):
    """Returns set of full hashes to drop (both revert and original)"""
    drops = set()
    revert_pattern = re.compile(r'^Revert "')
    revert_hash_pattern = re.compile(r'This reverts commit ([a-f0-9]+)')
    commit_map = {full: (short, subject) for short, full, subject in commits}

    for short, full, subject in commits:
        if not revert_pattern.search(subject):
            continue

        msg = get_commit_message(full)
        m = revert_hash_pattern.search(msg)
        if m:
            reverted_hash = m.group(1)
            # Check if original is in our commit range
            if reverted_hash in commit_map:
                drops.add(full)
                drops.add(reverted_hash)
                orig_short = commit_map[reverted_hash][0]
                print(f"  DROP revert pair: {short} (revert) + {orig_short} (original)")
            else:
                # Original not in our range (probably in edk2), just drop the revert
                drops.add(full)
                print(f"  DROP revert only: {short} (original {reverted_hash[:12]} not in range)")
        else:
            print(f"  WARN: revert {short} has no 'This reverts commit' line")

    return drops

def analyze_squash_on_rebase(commits):
    """Returns list of (squash_full_hash, target_full_hash_or_None)"""
    squash_pattern = re.compile(r'\[Squash On Rebase\]|\[SQUASH ON REBASE\]', re.IGNORECASE)
    target_hash_pattern = re.compile(r'(?:Squash (?:on|On) Rebase with|Commit to squash into:|squash with)\s*\n?\s*(?:https://github\.com/microsoft/mu_basecore/commit/)?([a-f0-9]+)', re.IGNORECASE)
    alt_squash_pattern = re.compile(r'(?:should be squashed with|Squash with)\s+([a-f0-9]+)', re.IGNORECASE)

    commit_map = {full: (short, subject) for short, full, subject in commits}
    # Also build subject->hash map for fallback matching
    subject_map = {}
    for short, full, subject in commits:
        # Strip the [SQUASH ON REBASE] prefix for matching
        clean_subject = re.sub(r'\[.*?\]\s*', '', subject).strip()
        subject_map[clean_subject] = full

    squashes = []
    for short, full, subject in commits:
        if not squash_pattern.search(subject):
            continue

        msg = get_commit_message(full)
        target_hash = None

        # Try standard patterns
        m = target_hash_pattern.search(msg)
        if m:
            candidate = m.group(1)
            # Find matching commit in range (could be prefix match)
            for cfull in commit_map:
                if cfull.startswith(candidate):
                    target_hash = cfull
                    break
            if not target_hash:
                print(f"  SQUASH {short} -> target {candidate[:12]} not in range, keeping as pick")
        else:
            # Try alternate pattern like "Squash with <hash>"
            m = alt_squash_pattern.search(msg)
            if m:
                candidate = m.group(1)
                for cfull in commit_map:
                    if cfull.startswith(candidate):
                        target_hash = cfull
                        break
                if not target_hash:
                    print(f"  SQUASH {short} -> target {candidate[:12]} not in range, keeping as pick")
            else:
                # Check for "This reverts commit" pattern (squash-revert)
                revert_m = re.search(r'This reverts commit ([a-f0-9]+)', msg)
                if revert_m:
                    candidate = revert_m.group(1)
                    for cfull in commit_map:
                        if cfull.startswith(candidate):
                            target_hash = cfull
                            break
                    if target_hash:
                        print(f"  SQUASH-REVERT {short} -> squash into {target_hash[:12]}")
                    else:
                        print(f"  SQUASH-REVERT {short} -> target {candidate[:12]} not in range, keeping as pick")
                else:
                    print(f"  SQUASH {short} -> no target found in message, keeping as pick")

        if target_hash:
            target_short = commit_map[target_hash][0]
            print(f"  SQUASH {short} -> into {target_short}")

        squashes.append((full, target_hash))

    return squashes

def generate_todo_processor(todo_file_path):
    """Generate the processed todo file"""
    print("Analyzing 513 commits...")
    commits = get_all_commits()
    print(f"Found {len(commits)} commits")

    print("\n=== Cherry-Pick Analysis ===")
    cherry_drops = analyze_cherry_picks(commits)
    print(f"Cherry-picks to drop: {len(cherry_drops)}")

    print("\n=== Revert Analysis ===")
    revert_drops = analyze_reverts(commits)
    print(f"Reverts to drop (including originals): {len(revert_drops)}")

    print("\n=== Squash On Rebase Analysis ===")
    squashes = analyze_squash_on_rebase(commits)
    print(f"Squash operations: {len(squashes)}")

    all_drops = cherry_drops | revert_drops
    # Also drop squash-on-rebase commits that are ALSO cherry-picks being dropped
    # (like d5a9eeef9f which is both CHERRY-PICK and SQUASH ON REBASE)

    print(f"\nTotal commits to drop: {len(all_drops)}")
    print(f"Squash operations to perform: {len([s for s in squashes if s[1] is not None])}")

    # Write the data files for the sequence editor script
    with open(os.path.join(r"Q:\code\mu_basecore", "rebase_drops.txt"), "w") as f:
        for h in all_drops:
            f.write(f"{h[:12]}\n")

    with open(os.path.join(r"Q:\code\mu_basecore", "rebase_squashes.txt"), "w") as f:
        for squash_hash, target_hash in squashes:
            if squash_hash in all_drops:
                continue  # Already being dropped
            if target_hash and target_hash not in all_drops:
                f.write(f"{squash_hash[:12]}|{target_hash[:12]}\n")

    print("\nWrote rebase_drops.txt and rebase_squashes.txt")

if __name__ == "__main__":
    generate_todo_processor(sys.argv[1] if len(sys.argv) > 1 else None)
