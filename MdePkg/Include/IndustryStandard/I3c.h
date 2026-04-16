/** @file
  I3C I/O Protocol.

  The EFI I3C I/O Protocol enables upper-layer drivers to communicate with a
  single I3C device without knowledge of the underlying host controller or bus
  topology.  The I3C bus driver installs one instance on each child handle it
  creates during device enumeration.

  Copyright (c) Microsoft Corporation. All rights reserved.<BR>
  SPDX-License-Identifier: BSD-2-Clause-Patent

**/

#ifndef __I3C_IO_H__
#define __I3C_IO_H__

#include <Protocol/I3cEnumerate.h>
#include <Protocol/I3cHost.h>

#define EFI_I3C_IO_PROTOCOL_GUID \
  { 0x4a6c8e7d, 0x2b3f, 0x4e5a, \
    { 0x81, 0x9c, 0x3f, 0x7e, 0xb2, 0x15, 0xa4, 0x68 } }

typedef struct _EFI_I3C_IO_PROTOCOL EFI_I3C_IO_PROTOCOL;

// ============================================================================
//  Protocol Function Types
// ============================================================================

/**
  Queue an I3C transaction for execution on the device represented by This.

  The bus driver translates this call into a host-level request using the
  device's bus configuration index and dynamic address.

  This routine must be called at or below TPL_NOTIFY.  For synchronous
  requests (Event == NULL) it must be called at or below TPL_CALLBACK.

  When Event is NULL, QueueRequest() operates synchronously and returns
  the I3C completion status directly.

  When Event is not NULL, QueueRequest() returns EFI_SUCCESS immediately
  and signals Event on completion.  The optional I3cStatus buffer receives
  the final status.

  @param[in]  This           Pointer to an EFI_I3C_IO_PROTOCOL instance.
  @param[in]  Event          Event to signal on async completion, or NULL
                             for synchronous operation.
  @param[in]  RequestPacket  Pointer to an I3C_REQUEST_PACKET describing
                             the transaction.
  @param[out] I3cStatus      Optional buffer to receive the async completion
                             status.

  @retval EFI_SUCCESS           Transaction completed or queued.
  @retval EFI_BAD_BUFFER_SIZE   An operation length exceeds controller limits.
  @retval EFI_DEVICE_ERROR      A bus error occurred.
  @retval EFI_INVALID_PARAMETER RequestPacket is NULL.
  @retval EFI_NO_MAPPING        Bus configuration could not be applied.
  @retval EFI_NO_RESPONSE       Device did not respond.
  @retval EFI_OUT_OF_RESOURCES  Insufficient memory.
  @retval EFI_UNSUPPORTED       Transaction type not supported.

**/
typedef
EFI_STATUS
(EFIAPI *EFI_I3C_IO_PROTOCOL_QUEUE_REQUEST)(
  IN CONST EFI_I3C_IO_PROTOCOL  *This,
  IN EFI_EVENT                  Event          OPTIONAL,
  IN I3C_REQUEST_PACKET         *RequestPacket,
  OUT EFI_STATUS                *I3cStatus     OPTIONAL
  );

// ============================================================================
//  Protocol Structure
// ============================================================================

///
/// I3C I/O Protocol
///
/// One instance is installed per I3C device child handle.  Upper-layer device
/// drivers locate and open this protocol to perform transactions with the
/// device without knowing which controller or bus it is attached to.
///
struct _EFI_I3C_IO_PROTOCOL {
  ///
  /// Queue an I3C transaction for execution on this device.
  ///
  EFI_I3C_IO_PROTOCOL_QUEUE_REQUEST        QueueRequest;

  ///
  /// Vendor-defined GUID identifying the device type.
  ///
  CONST EFI_GUID                           *DeviceGuid;

  ///
  /// Disambiguating index when multiple instances of DeviceGuid exist.
  ///
  UINT32                                   DeviceIndex;

  ///
  /// Hardware revision of the device.
  ///
  UINT32                                   HardwareRevision;

  ///
  /// 48-bit Provisional ID read from the device via GETPID CCC.
  ///
  I3C_PROVISIONAL_ID                       ProvisionalId;

  ///
  /// Bus Characteristics Register (BCR) value from GETBCR CCC.
  ///
  UINT8                                    BusCharacteristics;

  ///
  /// Device Characteristics Register (DCR) value from GETDCR CCC.
  ///
  UINT8                                    DeviceCharacteristics;

  ///
  /// 7-bit dynamic address assigned to this device.
  ///
  UINT8                                    DynamicAddress;

  ///
  /// Capabilities of the underlying I3C host controller.
  ///
  CONST EFI_I3C_CONTROLLER_CAPABILITIES    *I3cControllerCapabilities;
};

///
/// Reference to variable defined in the .DEC file
///
extern EFI_GUID  gEfiI3cIoProtocolGuid;

#endif //  __I3C_IO_H__
