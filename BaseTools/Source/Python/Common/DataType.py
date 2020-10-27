## @file
# This file is used to define common static strings used by INF/DEC/DSC files
#
# Copyright (c) 2007 - 2018, Intel Corporation. All rights reserved.<BR>
# Portions copyright (c) 2011 - 2013, ARM Ltd. All rights reserved.<BR>
# Portions Copyright (c) 2020, Hewlett Packard Enterprise Development LP. All rights reserved.<BR>
# SPDX-License-Identifier: BSD-2-Clause-Patent

##
# Common Definitions
#
TAB_SPLIT = '.'
TAB_COMMENT_EDK_START = '/*'
TAB_COMMENT_EDK_END = '*/'
TAB_COMMENT_EDK_SPLIT = '//'
TAB_COMMENT_SPLIT = '#'
TAB_SPECIAL_COMMENT = '##'
TAB_EQUAL_SPLIT = '='
TAB_VALUE_SPLIT = '|'
TAB_COMMA_SPLIT = ','
TAB_SPACE_SPLIT = ' '
TAB_SEMI_COLON_SPLIT = ';'
TAB_SECTION_START = '['
TAB_SECTION_END = ']'
TAB_OPTION_START = '<'
TAB_OPTION_END = '>'
TAB_SLASH = '\\'
TAB_BACK_SLASH = '/'
TAB_STAR = '*'
TAB_LINE_BREAK = '\n'
TAB_PRINTCHAR_VT = '\x0b'
TAB_PRINTCHAR_BS = '\b'
TAB_PRINTCHAR_NUL = '\0'
TAB_UINT8 = 'UINT8'
TAB_UINT16 = 'UINT16'
TAB_UINT32 = 'UINT32'
TAB_UINT64 = 'UINT64'
TAB_VOID = 'VOID*'
TAB_GUID = 'GUID'

TAB_PCD_CLEAN_NUMERIC_TYPES = {TAB_UINT8, TAB_UINT16, TAB_UINT32, TAB_UINT64}
TAB_PCD_NUMERIC_TYPES = {TAB_UINT8, TAB_UINT16, TAB_UINT32, TAB_UINT64, 'BOOLEAN'}
TAB_PCD_NUMERIC_TYPES_VOID = {TAB_UINT8, TAB_UINT16, TAB_UINT32, TAB_UINT64, 'BOOLEAN', TAB_VOID}

TAB_WORKSPACE = '$(WORKSPACE)'
TAB_FV_DIRECTORY = 'FV'

TAB_ARCH_NULL = ''
TAB_ARCH_COMMON = 'COMMON'
TAB_ARCH_IA32 = 'IA32'
TAB_ARCH_X64 = 'X64'
TAB_ARCH_ARM = 'ARM'
TAB_ARCH_EBC = 'EBC'
TAB_ARCH_AARCH64 = 'AARCH64'

TAB_ARCH_RISCV64 = 'RISCV64'

ARCH_SET_FULL = {TAB_ARCH_IA32, TAB_ARCH_X64, TAB_ARCH_ARM, TAB_ARCH_EBC, TAB_ARCH_AARCH64, TAB_ARCH_RISCV64, TAB_ARCH_COMMON}

SUP_MODULE_BASE = 'BASE'
SUP_MODULE_SEC = 'SEC'
SUP_MODULE_PEI_CORE = 'PEI_CORE'
SUP_MODULE_PEIM = 'PEIM'
SUP_MODULE_DXE_CORE = 'DXE_CORE'
SUP_MODULE_DXE_DRIVER = 'DXE_DRIVER'
SUP_MODULE_DXE_RUNTIME_DRIVER = 'DXE_RUNTIME_DRIVER'
SUP_MODULE_DXE_SAL_DRIVER = 'DXE_SAL_DRIVER'
SUP_MODULE_DXE_SMM_DRIVER = 'DXE_SMM_DRIVER'
SUP_MODULE_UEFI_DRIVER = 'UEFI_DRIVER'
SUP_MODULE_UEFI_APPLICATION = 'UEFI_APPLICATION'
SUP_MODULE_USER_DEFINED = 'USER_DEFINED'
SUP_MODULE_HOST_APPLICATION = 'HOST_APPLICATION'
SUP_MODULE_SMM_CORE = 'SMM_CORE'
SUP_MODULE_MM_STANDALONE = 'MM_STANDALONE'
SUP_MODULE_MM_CORE_STANDALONE = 'MM_CORE_STANDALONE'

SUP_MODULE_LIST = [SUP_MODULE_BASE, SUP_MODULE_SEC, SUP_MODULE_PEI_CORE, SUP_MODULE_PEIM, SUP_MODULE_DXE_CORE, SUP_MODULE_DXE_DRIVER, \
                   SUP_MODULE_DXE_RUNTIME_DRIVER, SUP_MODULE_DXE_SAL_DRIVER, SUP_MODULE_DXE_SMM_DRIVER, SUP_MODULE_UEFI_DRIVER, \
                   SUP_MODULE_UEFI_APPLICATION, SUP_MODULE_USER_DEFINED, SUP_MODULE_HOST_APPLICATION, SUP_MODULE_SMM_CORE, SUP_MODULE_MM_STANDALONE, SUP_MODULE_MM_CORE_STANDALONE]
SUP_MODULE_LIST_STRING = TAB_VALUE_SPLIT.join(SUP_MODULE_LIST)
SUP_MODULE_SET_PEI = {SUP_MODULE_PEIM, SUP_MODULE_PEI_CORE}

EDK_COMPONENT_TYPE_LIBRARY = 'LIBRARY'
EDK_COMPONENT_TYPE_SECURITY_CORE = 'SECURITY_CORE'
EDK_COMPONENT_TYPE_PEI_CORE = SUP_MODULE_PEI_CORE
EDK_COMPONENT_TYPE_COMBINED_PEIM_DRIVER = 'COMBINED_PEIM_DRIVER'
EDK_COMPONENT_TYPE_PIC_PEIM = 'PIC_PEIM'
EDK_COMPONENT_TYPE_RELOCATABLE_PEIM = 'RELOCATABLE_PEIM'
EDK_COMPONENT_TYPE_BS_DRIVER = 'BS_DRIVER'
EDK_COMPONENT_TYPE_RT_DRIVER = 'RT_DRIVER'
EDK_COMPONENT_TYPE_SAL_RT_DRIVER = 'SAL_RT_DRIVER'
EDK_COMPONENT_TYPE_APPLICATION = 'APPLICATION'
EDK_NAME = 'EDK'
EDKII_NAME = 'EDKII'
MSG_EDKII_MAIL_ADDR = 'devel@edk2.groups.io'

COMPONENT_TO_MODULE_MAP_DICT = {
    EDK_COMPONENT_TYPE_LIBRARY               :   SUP_MODULE_BASE,
    EDK_COMPONENT_TYPE_SECURITY_CORE         :   SUP_MODULE_SEC,
    EDK_COMPONENT_TYPE_PEI_CORE              :   SUP_MODULE_PEI_CORE,
    EDK_COMPONENT_TYPE_COMBINED_PEIM_DRIVER  :   SUP_MODULE_PEIM,
    EDK_COMPONENT_TYPE_PIC_PEIM              :   SUP_MODULE_PEIM,
    EDK_COMPONENT_TYPE_RELOCATABLE_PEIM      :   SUP_MODULE_PEIM,
    "PE32_PEIM"                              :   SUP_MODULE_PEIM,
    EDK_COMPONENT_TYPE_BS_DRIVER             :   SUP_MODULE_DXE_DRIVER,
    EDK_COMPONENT_TYPE_RT_DRIVER             :   SUP_MODULE_DXE_RUNTIME_DRIVER,
    EDK_COMPONENT_TYPE_SAL_RT_DRIVER         :   SUP_MODULE_DXE_SAL_DRIVER,
    EDK_COMPONENT_TYPE_APPLICATION           :   SUP_MODULE_UEFI_APPLICATION,
    "LOGO"                                   :   SUP_MODULE_BASE,
}

BINARY_FILE_TYPE_FW = 'FW'
BINARY_FILE_TYPE_GUID = 'GUID'
BINARY_FILE_TYPE_PREEFORM = 'PREEFORM'
BINARY_FILE_TYPE_UEFI_APP = 'UEFI_APP'
BINARY_FILE_TYPE_UNI_UI = 'UNI_UI'
BINARY_FILE_TYPE_UNI_VER = 'UNI_VER'
BINARY_FILE_TYPE_LIB = 'LIB'
BINARY_FILE_TYPE_PE32 = 'PE32'
BINARY_FILE_TYPE_PIC = 'PIC'
BINARY_FILE_TYPE_PEI_DEPEX = 'PEI_DEPEX'
BINARY_FILE_TYPE_DXE_DEPEX = 'DXE_DEPEX'
BINARY_FILE_TYPE_SMM_DEPEX = 'SMM_DEPEX'
BINARY_FILE_TYPE_TE = 'TE'
BINARY_FILE_TYPE_VER = 'VER'
BINARY_FILE_TYPE_UI = 'UI'
BINARY_FILE_TYPE_BIN = 'BIN'
BINARY_FILE_TYPE_FV = 'FV'
BINARY_FILE_TYPE_RAW = 'RAW_BINARY'

PLATFORM_COMPONENT_TYPE_LIBRARY_CLASS = 'LIBRARY_CLASS'
PLATFORM_COMPONENT_TYPE_MODULE = 'MODULE'

TAB_SOURCES = 'Sources'
TAB_SOURCES_COMMON = TAB_SOURCES + TAB_SPLIT + TAB_ARCH_COMMON
TAB_SOURCES_IA32 = TAB_SOURCES + TAB_SPLIT + TAB_ARCH_IA32
TAB_SOURCES_X64 = TAB_SOURCES + TAB_SPLIT + TAB_ARCH_X64
TAB_SOURCES_ARM = TAB_SOURCES + TAB_SPLIT + TAB_ARCH_ARM
TAB_SOURCES_EBC = TAB_SOURCES + TAB_SPLIT + TAB_ARCH_EBC
TAB_SOURCES_AARCH64 = TAB_SOURCES + TAB_SPLIT + TAB_ARCH_AARCH64

TAB_BINARIES = 'Binaries'
TAB_BINARIES_COMMON = TAB_BINARIES + TAB_SPLIT + TAB_ARCH_COMMON
TAB_BINARIES_IA32 = TAB_BINARIES + TAB_SPLIT + TAB_ARCH_IA32
TAB_BINARIES_X64 = TAB_BINARIES + TAB_SPLIT + TAB_ARCH_X64
TAB_BINARIES_ARM = TAB_BINARIES + TAB_SPLIT + TAB_ARCH_ARM
TAB_BINARIES_EBC = TAB_BINARIES + TAB_SPLIT + TAB_ARCH_EBC
TAB_BINARIES_AARCH64 = TAB_BINARIES + TAB_SPLIT + TAB_ARCH_AARCH64

TAB_INCLUDES = 'Includes'
TAB_INCLUDES_COMMON = TAB_INCLUDES + TAB_SPLIT + TAB_ARCH_COMMON
TAB_INCLUDES_IA32 = TAB_INCLUDES + TAB_SPLIT + TAB_ARCH_IA32
TAB_INCLUDES_X64 = TAB_INCLUDES + TAB_SPLIT + TAB_ARCH_X64
TAB_INCLUDES_ARM = TAB_INCLUDES + TAB_SPLIT + TAB_ARCH_ARM
TAB_INCLUDES_EBC = TAB_INCLUDES + TAB_SPLIT + TAB_ARCH_EBC
TAB_INCLUDES_AARCH64 = TAB_INCLUDES + TAB_SPLIT + TAB_ARCH_AARCH64

TAB_GUIDS = 'Guids'
TAB_GUIDS_COMMON = TAB_GUIDS + TAB_SPLIT + TAB_ARCH_COMMON
TAB_GUIDS_IA32 = TAB_GUIDS + TAB_SPLIT + TAB_ARCH_IA32
TAB_GUIDS_X64 = TAB_GUIDS + TAB_SPLIT + TAB_ARCH_X64
TAB_GUIDS_ARM = TAB_GUIDS + TAB_SPLIT + TAB_ARCH_ARM
TAB_GUIDS_EBC = TAB_GUIDS + TAB_SPLIT + TAB_ARCH_EBC
TAB_GUIDS_AARCH64 = TAB_GUIDS + TAB_SPLIT + TAB_ARCH_AARCH64

TAB_PROTOCOLS = 'Protocols'
TAB_PROTOCOLS_COMMON = TAB_PROTOCOLS + TAB_SPLIT + TAB_ARCH_COMMON
TAB_PROTOCOLS_IA32 = TAB_PROTOCOLS + TAB_SPLIT + TAB_ARCH_IA32
TAB_PROTOCOLS_X64 = TAB_PROTOCOLS + TAB_SPLIT + TAB_ARCH_X64
TAB_PROTOCOLS_ARM = TAB_PROTOCOLS + TAB_SPLIT + TAB_ARCH_ARM
TAB_PROTOCOLS_EBC = TAB_PROTOCOLS + TAB_SPLIT + TAB_ARCH_EBC
TAB_PROTOCOLS_AARCH64 = TAB_PROTOCOLS + TAB_SPLIT + TAB_ARCH_AARCH64

TAB_PPIS = 'Ppis'
TAB_PPIS_COMMON = TAB_PPIS + TAB_SPLIT + TAB_ARCH_COMMON
TAB_PPIS_IA32 = TAB_PPIS + TAB_SPLIT + TAB_ARCH_IA32
TAB_PPIS_X64 = TAB_PPIS + TAB_SPLIT + TAB_ARCH_X64
TAB_PPIS_ARM = TAB_PPIS + TAB_SPLIT + TAB_ARCH_ARM
TAB_PPIS_EBC = TAB_PPIS + TAB_SPLIT + TAB_ARCH_EBC
TAB_PPIS_AARCH64 = TAB_PPIS + TAB_SPLIT + TAB_ARCH_AARCH64

TAB_LIBRARY_CLASSES = 'LibraryClasses'
TAB_LIBRARY_CLASSES_COMMON = TAB_LIBRARY_CLASSES + TAB_SPLIT + TAB_ARCH_COMMON
TAB_LIBRARY_CLASSES_IA32 = TAB_LIBRARY_CLASSES + TAB_SPLIT + TAB_ARCH_IA32
TAB_LIBRARY_CLASSES_X64 = TAB_LIBRARY_CLASSES + TAB_SPLIT + TAB_ARCH_X64
TAB_LIBRARY_CLASSES_ARM = TAB_LIBRARY_CLASSES + TAB_SPLIT + TAB_ARCH_ARM
TAB_LIBRARY_CLASSES_EBC = TAB_LIBRARY_CLASSES + TAB_SPLIT + TAB_ARCH_EBC
TAB_LIBRARY_CLASSES_AARCH64 = TAB_LIBRARY_CLASSES + TAB_SPLIT + TAB_ARCH_AARCH64

TAB_PACKAGES = 'Packages'
TAB_PACKAGES_COMMON = TAB_PACKAGES + TAB_SPLIT + TAB_ARCH_COMMON
TAB_PACKAGES_IA32 = TAB_PACKAGES + TAB_SPLIT + TAB_ARCH_IA32
TAB_PACKAGES_X64 = TAB_PACKAGES + TAB_SPLIT + TAB_ARCH_X64
TAB_PACKAGES_ARM = TAB_PACKAGES + TAB_SPLIT + TAB_ARCH_ARM
TAB_PACKAGES_EBC = TAB_PACKAGES + TAB_SPLIT + TAB_ARCH_EBC
TAB_PACKAGES_AARCH64 = TAB_PACKAGES + TAB_SPLIT + TAB_ARCH_AARCH64

TAB_PCDS = 'Pcds'
TAB_PCDS_FIXED_AT_BUILD = 'FixedAtBuild'
TAB_PCDS_PATCHABLE_IN_MODULE = 'PatchableInModule'
TAB_PCDS_FEATURE_FLAG = 'FeatureFlag'
TAB_PCDS_DYNAMIC_EX = 'DynamicEx'
TAB_PCDS_DYNAMIC_EX_DEFAULT = 'DynamicExDefault'
TAB_PCDS_DYNAMIC_EX_VPD = 'DynamicExVpd'
TAB_PCDS_DYNAMIC_EX_HII = 'DynamicExHii'
TAB_PCDS_DYNAMIC = 'Dynamic'
TAB_PCDS_DYNAMIC_DEFAULT = 'DynamicDefault'
TAB_PCDS_DYNAMIC_VPD = 'DynamicVpd'
TAB_PCDS_DYNAMIC_HII = 'DynamicHii'

PCD_DYNAMIC_TYPE_SET = {TAB_PCDS_DYNAMIC, TAB_PCDS_DYNAMIC_DEFAULT, TAB_PCDS_DYNAMIC_VPD, TAB_PCDS_DYNAMIC_HII}
PCD_DYNAMIC_EX_TYPE_SET = {TAB_PCDS_DYNAMIC_EX, TAB_PCDS_DYNAMIC_EX_DEFAULT, TAB_PCDS_DYNAMIC_EX_VPD, TAB_PCDS_DYNAMIC_EX_HII}

# leave as a list for order
PCD_TYPE_LIST = [TAB_PCDS_FIXED_AT_BUILD, TAB_PCDS_PATCHABLE_IN_MODULE, TAB_PCDS_FEATURE_FLAG, TAB_PCDS_DYNAMIC, TAB_PCDS_DYNAMIC_EX]

TAB_PCDS_FIXED_AT_BUILD_NULL = TAB_PCDS + TAB_PCDS_FIXED_AT_BUILD
TAB_PCDS_FIXED_AT_BUILD_COMMON = TAB_PCDS + TAB_PCDS_FIXED_AT_BUILD + TAB_SPLIT + TAB_ARCH_COMMON
TAB_PCDS_FIXED_AT_BUILD_IA32 = TAB_PCDS + TAB_PCDS_FIXED_AT_BUILD + TAB_SPLIT + TAB_ARCH_IA32
TAB_PCDS_FIXED_AT_BUILD_X64 = TAB_PCDS + TAB_PCDS_FIXED_AT_BUILD + TAB_SPLIT + TAB_ARCH_X64
TAB_PCDS_FIXED_AT_BUILD_ARM = TAB_PCDS + TAB_PCDS_FIXED_AT_BUILD + TAB_SPLIT + TAB_ARCH_ARM
TAB_PCDS_FIXED_AT_BUILD_EBC = TAB_PCDS + TAB_PCDS_FIXED_AT_BUILD + TAB_SPLIT + TAB_ARCH_EBC
TAB_PCDS_FIXED_AT_BUILD_AARCH64 = TAB_PCDS + TAB_PCDS_FIXED_AT_BUILD + TAB_SPLIT + TAB_ARCH_AARCH64

TAB_PCDS_PATCHABLE_IN_MODULE_NULL = TAB_PCDS + TAB_PCDS_PATCHABLE_IN_MODULE
TAB_PCDS_PATCHABLE_IN_MODULE_COMMON = TAB_PCDS + TAB_PCDS_PATCHABLE_IN_MODULE + TAB_SPLIT + TAB_ARCH_COMMON
TAB_PCDS_PATCHABLE_IN_MODULE_IA32 = TAB_PCDS + TAB_PCDS_PATCHABLE_IN_MODULE + TAB_SPLIT + TAB_ARCH_IA32
TAB_PCDS_PATCHABLE_IN_MODULE_X64 = TAB_PCDS + TAB_PCDS_PATCHABLE_IN_MODULE + TAB_SPLIT + TAB_ARCH_X64
TAB_PCDS_PATCHABLE_IN_MODULE_ARM = TAB_PCDS + TAB_PCDS_PATCHABLE_IN_MODULE + TAB_SPLIT + TAB_ARCH_ARM
TAB_PCDS_PATCHABLE_IN_MODULE_EBC = TAB_PCDS + TAB_PCDS_PATCHABLE_IN_MODULE + TAB_SPLIT + TAB_ARCH_EBC
TAB_PCDS_PATCHABLE_IN_MODULE_AARCH64 = TAB_PCDS + TAB_PCDS_PATCHABLE_IN_MODULE + TAB_SPLIT + TAB_ARCH_AARCH64

TAB_PCDS_FEATURE_FLAG_NULL = TAB_PCDS + TAB_PCDS_FEATURE_FLAG
TAB_PCDS_FEATURE_FLAG_COMMON = TAB_PCDS + TAB_PCDS_FEATURE_FLAG + TAB_SPLIT + TAB_ARCH_COMMON
TAB_PCDS_FEATURE_FLAG_IA32 = TAB_PCDS + TAB_PCDS_FEATURE_FLAG + TAB_SPLIT + TAB_ARCH_IA32
TAB_PCDS_FEATURE_FLAG_X64 = TAB_PCDS + TAB_PCDS_FEATURE_FLAG + TAB_SPLIT + TAB_ARCH_X64
TAB_PCDS_FEATURE_FLAG_ARM = TAB_PCDS + TAB_PCDS_FEATURE_FLAG + TAB_SPLIT + TAB_ARCH_ARM
TAB_PCDS_FEATURE_FLAG_EBC = TAB_PCDS + TAB_PCDS_FEATURE_FLAG + TAB_SPLIT + TAB_ARCH_EBC
TAB_PCDS_FEATURE_FLAG_AARCH64 = TAB_PCDS + TAB_PCDS_FEATURE_FLAG + TAB_SPLIT + TAB_ARCH_AARCH64

TAB_PCDS_DYNAMIC_EX_NULL = TAB_PCDS + TAB_PCDS_DYNAMIC_EX
TAB_PCDS_DYNAMIC_EX_DEFAULT_NULL = TAB_PCDS + TAB_PCDS_DYNAMIC_EX_DEFAULT
TAB_PCDS_DYNAMIC_EX_HII_NULL = TAB_PCDS + TAB_PCDS_DYNAMIC_EX_HII
TAB_PCDS_DYNAMIC_EX_VPD_NULL = TAB_PCDS + TAB_PCDS_DYNAMIC_EX_VPD
TAB_PCDS_DYNAMIC_EX_COMMON = TAB_PCDS + TAB_PCDS_DYNAMIC_EX + TAB_SPLIT + TAB_ARCH_COMMON
TAB_PCDS_DYNAMIC_EX_IA32 = TAB_PCDS + TAB_PCDS_DYNAMIC_EX + TAB_SPLIT + TAB_ARCH_IA32
TAB_PCDS_DYNAMIC_EX_X64 = TAB_PCDS + TAB_PCDS_DYNAMIC_EX + TAB_SPLIT + TAB_ARCH_X64
TAB_PCDS_DYNAMIC_EX_ARM = TAB_PCDS + TAB_PCDS_DYNAMIC_EX + TAB_SPLIT + TAB_ARCH_ARM
TAB_PCDS_DYNAMIC_EX_EBC = TAB_PCDS + TAB_PCDS_DYNAMIC_EX + TAB_SPLIT + TAB_ARCH_EBC
TAB_PCDS_DYNAMIC_EX_AARCH64 = TAB_PCDS + TAB_PCDS_DYNAMIC_EX + TAB_SPLIT + TAB_ARCH_AARCH64

TAB_PCDS_DYNAMIC_NULL = TAB_PCDS + TAB_PCDS_DYNAMIC
TAB_PCDS_DYNAMIC_DEFAULT_NULL = TAB_PCDS + TAB_PCDS_DYNAMIC_DEFAULT
TAB_PCDS_DYNAMIC_HII_NULL = TAB_PCDS + TAB_PCDS_DYNAMIC_HII
TAB_PCDS_DYNAMIC_VPD_NULL = TAB_PCDS + TAB_PCDS_DYNAMIC_VPD
TAB_PCDS_DYNAMIC_COMMON = TAB_PCDS + TAB_PCDS_DYNAMIC + TAB_SPLIT + TAB_ARCH_COMMON
TAB_PCDS_DYNAMIC_IA32 = TAB_PCDS + TAB_PCDS_DYNAMIC + TAB_SPLIT + TAB_ARCH_IA32
TAB_PCDS_DYNAMIC_X64 = TAB_PCDS + TAB_PCDS_DYNAMIC + TAB_SPLIT + TAB_ARCH_X64
TAB_PCDS_DYNAMIC_ARM = TAB_PCDS + TAB_PCDS_DYNAMIC + TAB_SPLIT + TAB_ARCH_ARM
TAB_PCDS_DYNAMIC_EBC = TAB_PCDS + TAB_PCDS_DYNAMIC + TAB_SPLIT + TAB_ARCH_EBC
TAB_PCDS_DYNAMIC_AARCH64 = TAB_PCDS + TAB_PCDS_DYNAMIC + TAB_SPLIT + TAB_ARCH_AARCH64

TAB_PCDS_PATCHABLE_LOAD_FIX_ADDRESS_PEI_PAGE_SIZE = 'PcdLoadFixAddressPeiCodePageNumber'
TAB_PCDS_PATCHABLE_LOAD_FIX_ADDRESS_PEI_PAGE_SIZE_DATA_TYPE = 'UINT32'
TAB_PCDS_PATCHABLE_LOAD_FIX_ADDRESS_DXE_PAGE_SIZE = 'PcdLoadFixAddressBootTimeCodePageNumber'
TAB_PCDS_PATCHABLE_LOAD_FIX_ADDRESS_DXE_PAGE_SIZE_DATA_TYPE = 'UINT32'
TAB_PCDS_PATCHABLE_LOAD_FIX_ADDRESS_RUNTIME_PAGE_SIZE = 'PcdLoadFixAddressRuntimeCodePageNumber'
TAB_PCDS_PATCHABLE_LOAD_FIX_ADDRESS_RUNTIME_PAGE_SIZE_DATA_TYPE = 'UINT32'
TAB_PCDS_PATCHABLE_LOAD_FIX_ADDRESS_SMM_PAGE_SIZE = 'PcdLoadFixAddressSmmCodePageNumber'
TAB_PCDS_PATCHABLE_LOAD_FIX_ADDRESS_SMM_PAGE_SIZE_DATA_TYPE = 'UINT32'
TAB_PCDS_PATCHABLE_LOAD_FIX_ADDRESS_SET =  {TAB_PCDS_PATCHABLE_LOAD_FIX_ADDRESS_PEI_PAGE_SIZE, \
                                            TAB_PCDS_PATCHABLE_LOAD_FIX_ADDRESS_DXE_PAGE_SIZE, \
                                            TAB_PCDS_PATCHABLE_LOAD_FIX_ADDRESS_RUNTIME_PAGE_SIZE, \
                                            TAB_PCDS_PATCHABLE_LOAD_FIX_ADDRESS_SMM_PAGE_SIZE}

## The mapping dictionary from datum type to its maximum number.
MAX_VAL_TYPE = {"BOOLEAN":0x01, TAB_UINT8:0xFF, TAB_UINT16:0xFFFF, TAB_UINT32:0xFFFFFFFF, TAB_UINT64:0xFFFFFFFFFFFFFFFF}
## The mapping dictionary from datum type to size string.
MAX_SIZE_TYPE = {"BOOLEAN":1, TAB_UINT8:1, TAB_UINT16:2, TAB_UINT32:4, TAB_UINT64:8}

TAB_DEPEX = 'Depex'
TAB_DEPEX_COMMON = TAB_DEPEX + TAB_SPLIT + TAB_ARCH_COMMON
TAB_DEPEX_IA32 = TAB_DEPEX + TAB_SPLIT + TAB_ARCH_IA32
TAB_DEPEX_X64 = TAB_DEPEX + TAB_SPLIT + TAB_ARCH_X64
TAB_DEPEX_ARM = TAB_DEPEX + TAB_SPLIT + TAB_ARCH_ARM
TAB_DEPEX_EBC = TAB_DEPEX + TAB_SPLIT + TAB_ARCH_EBC
TAB_DEPEX_AARCH64 = TAB_DEPEX + TAB_SPLIT + TAB_ARCH_AARCH64

TAB_SKUIDS = 'SkuIds'
TAB_DEFAULT_STORES = 'DefaultStores'
TAB_DEFAULT_STORES_DEFAULT = 'STANDARD'

TAB_LIBRARIES = 'Libraries'
TAB_LIBRARIES_COMMON = TAB_LIBRARIES + TAB_SPLIT + TAB_ARCH_COMMON
TAB_LIBRARIES_IA32 = TAB_LIBRARIES + TAB_SPLIT + TAB_ARCH_IA32
TAB_LIBRARIES_X64 = TAB_LIBRARIES + TAB_SPLIT + TAB_ARCH_X64
TAB_LIBRARIES_ARM = TAB_LIBRARIES + TAB_SPLIT + TAB_ARCH_ARM
TAB_LIBRARIES_EBC = TAB_LIBRARIES + TAB_SPLIT + TAB_ARCH_EBC
TAB_LIBRARIES_AARCH64 = TAB_LIBRARIES + TAB_SPLIT + TAB_ARCH_AARCH64

TAB_COMPONENTS = 'Components'
TAB_COMPONENTS_COMMON = TAB_COMPONENTS + TAB_SPLIT + TAB_ARCH_COMMON
TAB_COMPONENTS_IA32 = TAB_COMPONENTS + TAB_SPLIT + TAB_ARCH_IA32
TAB_COMPONENTS_X64 = TAB_COMPONENTS + TAB_SPLIT + TAB_ARCH_X64
TAB_COMPONENTS_ARM = TAB_COMPONENTS + TAB_SPLIT + TAB_ARCH_ARM
TAB_COMPONENTS_EBC = TAB_COMPONENTS + TAB_SPLIT + TAB_ARCH_EBC
TAB_COMPONENTS_AARCH64 = TAB_COMPONENTS + TAB_SPLIT + TAB_ARCH_AARCH64

TAB_BUILD_OPTIONS = 'BuildOptions'

TAB_DEFINE = 'DEFINE'
TAB_NMAKE = 'Nmake'
TAB_USER_EXTENSIONS = 'UserExtensions'
TAB_INCLUDE = '!include'
TAB_DEFAULT = 'DEFAULT'
TAB_COMMON = 'COMMON'

#
# Common Define
#
TAB_COMMON_DEFINES = 'Defines'

#
# Inf Definitions
#
TAB_INF_DEFINES = TAB_COMMON_DEFINES
TAB_INF_DEFINES_INF_VERSION = 'INF_VERSION'
TAB_INF_DEFINES_BASE_NAME = 'BASE_NAME'
TAB_INF_DEFINES_FILE_GUID = 'FILE_GUID'
TAB_INF_DEFINES_MODULE_TYPE = 'MODULE_TYPE'
TAB_INF_DEFINES_EFI_SPECIFICATION_VERSION = 'EFI_SPECIFICATION_VERSION'
TAB_INF_DEFINES_UEFI_SPECIFICATION_VERSION = 'UEFI_SPECIFICATION_VERSION'
TAB_INF_DEFINES_PI_SPECIFICATION_VERSION = 'PI_SPECIFICATION_VERSION'
TAB_INF_DEFINES_EDK_RELEASE_VERSION = 'EDK_RELEASE_VERSION'
TAB_INF_DEFINES_BINARY_MODULE = 'BINARY_MODULE'
TAB_INF_DEFINES_LIBRARY_CLASS = 'LIBRARY_CLASS'
TAB_INF_DEFINES_COMPONENT_TYPE = 'COMPONENT_TYPE'
TAB_INF_DEFINES_MAKEFILE_NAME = 'MAKEFILE_NAME'
TAB_INF_DEFINES_DPX_SOURCE = 'DPX_SOURCE'
TAB_INF_DEFINES_BUILD_NUMBER = 'BUILD_NUMBER'
TAB_INF_DEFINES_BUILD_TYPE = 'BUILD_TYPE'
TAB_INF_DEFINES_FFS_EXT = 'FFS_EXT'
TAB_INF_DEFINES_FV_EXT = 'FV_EXT'
TAB_INF_DEFINES_SOURCE_FV = 'SOURCE_FV'
TAB_INF_DEFINES_VERSION_NUMBER = 'VERSION_NUMBER'
TAB_INF_DEFINES_VERSION = 'VERSION'          # for Edk inf, the same as VERSION_NUMBER
TAB_INF_DEFINES_VERSION_STRING = 'VERSION_STRING'
TAB_INF_DEFINES_PCD_IS_DRIVER = 'PCD_IS_DRIVER'
TAB_INF_DEFINES_TIANO_EDK_FLASHMAP_H = 'TIANO_EDK_FLASHMAP_H'
TAB_INF_DEFINES_ENTRY_POINT = 'ENTRY_POINT'
TAB_INF_DEFINES_UNLOAD_IMAGE = 'UNLOAD_IMAGE'
TAB_INF_DEFINES_CONSTRUCTOR = 'CONSTRUCTOR'
TAB_INF_DEFINES_DESTRUCTOR = 'DESTRUCTOR'
TAB_INF_DEFINES_DEFINE = 'DEFINE'
TAB_INF_DEFINES_SPEC = 'SPEC'
TAB_INF_DEFINES_CUSTOM_MAKEFILE = 'CUSTOM_MAKEFILE'
TAB_INF_DEFINES_MACRO = '__MACROS__'
TAB_INF_DEFINES_SHADOW = 'SHADOW'
TAB_INF_FIXED_PCD = 'FixedPcd'
TAB_INF_FEATURE_PCD = 'FeaturePcd'
TAB_INF_PATCH_PCD = 'PatchPcd'
TAB_INF_PCD = 'Pcd'
TAB_INF_PCD_EX = 'PcdEx'
TAB_INF_USAGE_PRO = 'PRODUCES'
TAB_INF_USAGE_SOME_PRO = 'SOMETIMES_PRODUCES'
TAB_INF_USAGE_CON = 'CONSUMES'
TAB_INF_USAGE_SOME_CON = 'SOMETIMES_CONSUMES'
TAB_INF_USAGE_NOTIFY = 'NOTIFY'
TAB_INF_USAGE_TO_START = 'TO_START'
TAB_INF_USAGE_BY_START = 'BY_START'
TAB_INF_GUIDTYPE_EVENT = 'Event'
TAB_INF_GUIDTYPE_FILE = 'File'
TAB_INF_GUIDTYPE_FV = 'FV'
TAB_INF_GUIDTYPE_GUID = 'GUID'
TAB_INF_GUIDTYPE_HII = 'HII'
TAB_INF_GUIDTYPE_HOB = 'HOB'
TAB_INF_GUIDTYPE_ST = 'SystemTable'
TAB_INF_GUIDTYPE_TSG = 'TokenSpaceGuid'
TAB_INF_GUIDTYPE_VAR = 'Variable'
TAB_INF_GUIDTYPE_PROTOCOL = 'PROTOCOL'
TAB_INF_GUIDTYPE_PPI = 'PPI'
TAB_INF_USAGE_UNDEFINED = 'UNDEFINED'

#
# Dec Definitions
#
TAB_DEC_DEFINES = TAB_COMMON_DEFINES
TAB_DEC_DEFINES_DEC_SPECIFICATION = 'DEC_SPECIFICATION'
TAB_DEC_DEFINES_PACKAGE_NAME = 'PACKAGE_NAME'
TAB_DEC_DEFINES_PACKAGE_GUID = 'PACKAGE_GUID'
TAB_DEC_DEFINES_PACKAGE_VERSION = 'PACKAGE_VERSION'
TAB_DEC_DEFINES_PKG_UNI_FILE = 'PKG_UNI_FILE'

#
# Dsc Definitions
#
TAB_DSC_DEFINES = TAB_COMMON_DEFINES
TAB_DSC_DEFINES_PLATFORM_NAME = 'PLATFORM_NAME'
TAB_DSC_DEFINES_PLATFORM_GUID = 'PLATFORM_GUID'
TAB_DSC_DEFINES_PLATFORM_VERSION = 'PLATFORM_VERSION'
TAB_DSC_DEFINES_DSC_SPECIFICATION = 'DSC_SPECIFICATION'
TAB_DSC_DEFINES_OUTPUT_DIRECTORY = 'OUTPUT_DIRECTORY'
TAB_DSC_DEFINES_SUPPORTED_ARCHITECTURES = 'SUPPORTED_ARCHITECTURES'
TAB_DSC_DEFINES_BUILD_TARGETS = 'BUILD_TARGETS'
TAB_DSC_DEFINES_SKUID_IDENTIFIER = 'SKUID_IDENTIFIER'
TAB_DSC_DEFINES_PCD_INFO_GENERATION = 'PCD_INFO_GENERATION'
TAB_DSC_DEFINES_PCD_DYNAMIC_AS_DYNAMICEX = 'PCD_DYNAMIC_AS_DYNAMICEX'
TAB_DSC_DEFINES_PCD_VAR_CHECK_GENERATION = 'PCD_VAR_CHECK_GENERATION'
TAB_DSC_DEFINES_VPD_AUTHENTICATED_VARIABLE_STORE = 'VPD_AUTHENTICATED_VARIABLE_STORE'
TAB_DSC_DEFINES_FLASH_DEFINITION = 'FLASH_DEFINITION'
TAB_DSC_DEFINES_BUILD_NUMBER = 'BUILD_NUMBER'
TAB_DSC_DEFINES_MAKEFILE_NAME = 'MAKEFILE_NAME'
TAB_DSC_DEFINES_BS_BASE_ADDRESS = 'BsBaseAddress'
TAB_DSC_DEFINES_RT_BASE_ADDRESS = 'RtBaseAddress'
TAB_DSC_DEFINES_RFC_LANGUAGES = 'RFC_LANGUAGES'
TAB_DSC_DEFINES_ISO_LANGUAGES = 'ISO_LANGUAGES'
TAB_DSC_DEFINES_DEFINE = 'DEFINE'
TAB_DSC_DEFINES_VPD_TOOL_GUID = 'VPD_TOOL_GUID'
TAB_FIX_LOAD_TOP_MEMORY_ADDRESS = 'FIX_LOAD_TOP_MEMORY_ADDRESS'
TAB_DSC_DEFINES_EDKGLOBAL = 'EDK_GLOBAL'
TAB_DSC_PREBUILD = 'PREBUILD'
TAB_DSC_POSTBUILD = 'POSTBUILD'
#
# TargetTxt Definitions
#
TAB_TAT_DEFINES_ACTIVE_PLATFORM = 'ACTIVE_PLATFORM'
TAB_TAT_DEFINES_ACTIVE_MODULE = 'ACTIVE_MODULE'
TAB_TAT_DEFINES_TOOL_CHAIN_CONF = 'TOOL_CHAIN_CONF'
TAB_TAT_DEFINES_MAX_CONCURRENT_THREAD_NUMBER = 'MAX_CONCURRENT_THREAD_NUMBER'
TAB_TAT_DEFINES_TARGET = 'TARGET'
TAB_TAT_DEFINES_TOOL_CHAIN_TAG = 'TOOL_CHAIN_TAG'
TAB_TAT_DEFINES_TARGET_ARCH = 'TARGET_ARCH'
TAB_TAT_DEFINES_BUILD_RULE_CONF = "BUILD_RULE_CONF"

#
# ToolDef Definitions
#
TAB_TOD_DEFINES_TARGET = 'TARGET'
TAB_TOD_DEFINES_TOOL_CHAIN_TAG = 'TOOL_CHAIN_TAG'
TAB_TOD_DEFINES_TARGET_ARCH = 'TARGET_ARCH'
TAB_TOD_DEFINES_COMMAND_TYPE = 'COMMAND_TYPE'
TAB_TOD_DEFINES_FAMILY = 'FAMILY'
TAB_TOD_DEFINES_BUILDRULEFAMILY = 'BUILDRULEFAMILY'
TAB_TOD_DEFINES_BUILDRULEORDER = 'BUILDRULEORDER'

#
# Conditional Statements
#
TAB_IF = '!if'
TAB_END_IF = '!endif'
TAB_ELSE_IF = '!elseif'
TAB_ELSE = '!else'
TAB_IF_DEF = '!ifdef'
TAB_IF_N_DEF = '!ifndef'
TAB_IF_EXIST = '!if exist'
TAB_ERROR = '!error'

#
# Unknown section
#
TAB_UNKNOWN = 'UNKNOWN'

#
# Build database path
#
DATABASE_PATH = ":memory:" #"BuildDatabase.db"

# used by ECC
MODIFIER_SET = {'IN', 'OUT', 'OPTIONAL', 'UNALIGNED', 'EFI_RUNTIMESERVICE', 'EFI_BOOTSERVICE', 'EFIAPI'}

# Dependency Opcodes
DEPEX_OPCODE_BEFORE = "BEFORE"
DEPEX_OPCODE_AFTER = "AFTER"
DEPEX_OPCODE_PUSH = "PUSH"
DEPEX_OPCODE_AND = "AND"
DEPEX_OPCODE_OR = "OR"
DEPEX_OPCODE_NOT = "NOT"
DEPEX_OPCODE_END = "END"
DEPEX_OPCODE_SOR = "SOR"
DEPEX_OPCODE_TRUE = "TRUE"
DEPEX_OPCODE_FALSE = "FALSE"

# Dependency Expression
DEPEX_SUPPORTED_OPCODE_SET = {"BEFORE", "AFTER", "PUSH", "AND", "OR", "NOT", "END", "SOR", "TRUE", "FALSE", '(', ')'}

TAB_STATIC_LIBRARY = "STATIC-LIBRARY-FILE"
TAB_DYNAMIC_LIBRARY = "DYNAMIC-LIBRARY-FILE"
TAB_FRAMEWORK_IMAGE = "EFI-IMAGE-FILE"
TAB_C_CODE_FILE = "C-CODE-FILE"
TAB_C_HEADER_FILE = "C-HEADER-FILE"
TAB_UNICODE_FILE = "UNICODE-TEXT-FILE"
TAB_IMAGE_FILE = "IMAGE-DEFINITION-FILE"
TAB_DEPENDENCY_EXPRESSION_FILE = "DEPENDENCY-EXPRESSION-FILE"
TAB_UNKNOWN_FILE = "UNKNOWN-TYPE-FILE"
TAB_DEFAULT_BINARY_FILE = "_BINARY_FILE_"
TAB_OBJECT_FILE = "OBJECT-FILE"
TAB_VFR_FILE = 'VISUAL-FORM-REPRESENTATION-FILE'
TAB_ARC_FILE = 'Resource-File'  # MU_CHANGE
TAB_VER_FILE = 'Version-Info-File' # MU_CHANGE

# used by BRG
TAB_BRG_PCD = 'PCD'
TAB_BRG_LIBRARY = 'Library'

#
# Build Rule File Version Definition
#
TAB_BUILD_RULE_VERSION = "build_rule_version"

# section name for PCDs
PCDS_DYNAMIC_DEFAULT = "PcdsDynamicDefault"
PCDS_DYNAMIC_VPD = "PcdsDynamicVpd"
PCDS_DYNAMIC_HII = "PcdsDynamicHii"
PCDS_DYNAMICEX_DEFAULT = "PcdsDynamicExDefault"
PCDS_DYNAMICEX_VPD = "PcdsDynamicExVpd"
PCDS_DYNAMICEX_HII = "PcdsDynamicExHii"

SECTIONS_HAVE_ITEM_PCD_SET = {PCDS_DYNAMIC_DEFAULT.upper(), PCDS_DYNAMIC_VPD.upper(), PCDS_DYNAMIC_HII.upper(), \
                              PCDS_DYNAMICEX_DEFAULT.upper(), PCDS_DYNAMICEX_VPD.upper(), PCDS_DYNAMICEX_HII.upper()}
# Section allowed to have items after arch
SECTIONS_HAVE_ITEM_AFTER_ARCH_SET = {TAB_LIBRARY_CLASSES.upper(), TAB_DEPEX.upper(), TAB_USER_EXTENSIONS.upper(),
                                 PCDS_DYNAMIC_DEFAULT.upper(),
                                 PCDS_DYNAMIC_VPD.upper(),
                                 PCDS_DYNAMIC_HII.upper(),
                                 PCDS_DYNAMICEX_DEFAULT.upper(),
                                 PCDS_DYNAMICEX_VPD.upper(),
                                 PCDS_DYNAMICEX_HII.upper(),
                                 TAB_BUILD_OPTIONS.upper(),
                                 TAB_PACKAGES.upper(),
                                 TAB_INCLUDES.upper()}

#
# pack codes as used in PcdDb and elsewhere
#
PACK_PATTERN_GUID = '=LHHBBBBBBBB'
PACK_CODE_BY_SIZE = {8:'=Q',
                     4:'=L',
                     2:'=H',
                     1:'=B',
                     0:'=B',
                    16:""}

TAB_COMPILER_MSFT = 'MSFT'
