/** @file
  Application for BigNumber Primitives Validation.

Copyright (c) 2022, Intel Corporation. All rights reserved.<BR>
SPDX-License-Identifier: BSD-2-Clause-Patent

**/

#include "TestBaseCryptLib.h"

//
// Debug data
//
#define MAX_TEST_DATA_SIZE    512
#define BYTES_OF_OPERATION_A  60
#define BITS_OF_OPERATION_A   480// (8 * 60)

GLOBAL_REMOVE_IF_UNREFERENCED CONST UINT8  BnOperationA[] = {
  0x00, 0x00, 0x00, 0x00, 0x93, 0x61, 0x7a, 0xba, 0xcc, 0x41, 0x73, 0x49, 0xae, 0x20, 0x41, 0x31,
  0x12, 0xe6, 0xfa, 0x4e, 0x89, 0xa9, 0x7e, 0xa2, 0x0a, 0x9e, 0xee, 0xe6, 0x4b, 0x55, 0xd3, 0x9a,
  0x21, 0x92, 0x99, 0x2a, 0x27, 0x4f, 0xc1, 0xa8, 0x36, 0xba, 0x3c, 0x23, 0xa3, 0xfe, 0xeb, 0xbd,
  0x45, 0x4d, 0x44, 0x23, 0x64, 0x3c, 0xe8, 0x0e, 0x2a, 0x9a, 0xc9, 0x4f, 0xa5, 0x4c, 0xa4, 0x9f
};

GLOBAL_REMOVE_IF_UNREFERENCED CONST UINT8  BnOperationB[] = {
  0xb0, 0x03, 0x61, 0xa3, 0x96, 0x17, 0x7a, 0x9c, 0xb4, 0x10, 0xff, 0x61, 0xf2, 0x00, 0x15, 0xad,
  0xcb, 0x00, 0x75, 0x3f, 0x45, 0xa3, 0x5e, 0x8b, 0xb5, 0xa0, 0x3d, 0x69, 0x9a, 0xc6, 0x50, 0x07,
  0x27, 0x2c, 0x32, 0xab, 0x0e, 0xde, 0xd1, 0x63, 0x1a, 0x8b, 0x60, 0x5a, 0x43, 0xff, 0x5b, 0xed,
  0x80, 0x86, 0x07, 0x2b, 0xa1, 0xe7, 0xcc, 0x23, 0x58, 0xba, 0xec, 0xa1, 0x34, 0xc8, 0x25, 0xa7
};

GLOBAL_REMOVE_IF_UNREFERENCED CONST UINT8  BnOperationC[] = {
  0x27, 0x2c, 0x32, 0xab, 0x0e, 0xde, 0xd1, 0x63, 0x1a, 0x8b, 0x60, 0x5a, 0x43, 0xff, 0x5b, 0xed
};

GLOBAL_REMOVE_IF_UNREFERENCED CONST UINT8  BnOperationExp[] = {
  0x27, 0x2c, 0x32, 0xab, 0x0e, 0xde, 0xd1, 0x63
};

GLOBAL_REMOVE_IF_UNREFERENCED CONST UINT8  BnOperationMod[] = {
  0x48, 0xbe, 0xcb, 0xd5, 0x36, 0x2e, 0x93, 0x0b, 0x51, 0x45, 0x9c, 0x7d, 0xe7, 0xfe, 0x47, 0xaa,
  0xc5, 0xd3, 0x4b, 0x4f, 0x06, 0x24, 0xb4, 0x31, 0x83, 0x55, 0xb5, 0xf0, 0xda, 0x14, 0xca, 0x46
};

// BnOperationA + BnOperationB
GLOBAL_REMOVE_IF_UNREFERENCED CONST UINT8  BnResultSum[] = {
  0xb0, 0x03, 0x61, 0xa4, 0x29, 0x78, 0xf5, 0x57, 0x80, 0x52, 0x72, 0xab, 0xa0, 0x20, 0x56, 0xde,
  0xdd, 0xe7, 0x6f, 0x8d, 0xcf, 0x4c, 0xdd, 0x2d, 0xc0, 0x3f, 0x2c, 0x4f, 0xe6, 0x1c, 0x23, 0xa1,
  0x48, 0xbe, 0xcb, 0xd5, 0x36, 0x2e, 0x93, 0x0b, 0x51, 0x45, 0x9c, 0x7d, 0xe7, 0xfe, 0x47, 0xaa,
  0xc5, 0xd3, 0x4b, 0x4f, 0x06, 0x24, 0xb4, 0x31, 0x83, 0x55, 0xb5, 0xf0, 0xda, 0x14, 0xca, 0x46
};

// (BnOperationA + BnOperationC) % BnOperationMod
GLOBAL_REMOVE_IF_UNREFERENCED CONST UINT8  BnResultSumMod[] =  {
  0x16, 0x0a, 0xcf, 0x78, 0x20, 0xac, 0x31, 0x53, 0xd9, 0x0f, 0x22, 0xfc, 0x08, 0x8d, 0xde, 0x0d,
  0x29, 0xf4, 0x07, 0xdd, 0xfa, 0xf5, 0x61, 0xd4, 0x1a, 0xe5, 0xa1, 0xef, 0x4a, 0x37, 0xfe, 0xec
};

// (BnOperationA * BnOperationC) % BnOperationMod
GLOBAL_REMOVE_IF_UNREFERENCED CONST UINT8  BnResultMulMod[] =  {
  0x01, 0xDB, 0xD2, 0x82, 0xC9, 0x24, 0x66, 0x2A, 0x96, 0x05, 0x11, 0xF2, 0x31, 0xF0, 0xCB, 0x28,
  0xBA, 0x5C, 0xBE, 0x7D, 0xEE, 0x37, 0x25, 0xB1, 0x24, 0x7E, 0x15, 0xAB, 0xCD, 0x86, 0x8E, 0x39
};

// BnOperationA / BnOperationMod
GLOBAL_REMOVE_IF_UNREFERENCED CONST UINT8  BnResultDiv[] =  {
  0x02, 0x06, 0xA6, 0xDC, 0x2E, 0x97, 0x05, 0xEA, 0xCD, 0xF7, 0xAB, 0xCD, 0xE5, 0x9C, 0x33, 0x03,
  0xCE, 0x3D, 0x7E, 0x63, 0x23, 0xB2, 0xEC, 0xED, 0x96, 0x9D, 0xC9, 0xBB, 0x78
};

// BnOperationA % BnOperationMod
GLOBAL_REMOVE_IF_UNREFERENCED CONST UINT8  BnResultMod[] =  {
  0x06, 0x2A, 0x8D, 0x06, 0x9D, 0x14, 0x53, 0x3B, 0x05, 0xD9, 0x86, 0x00, 0xA5, 0xB9, 0x05, 0x7F,
  0xC1, 0x82, 0xEC, 0x23, 0x44, 0x23, 0xC8, 0xA2, 0x42, 0xB3, 0x43, 0xB8, 0x7C, 0xD6, 0xB1, 0xCF
};

// BnOperationA % BnOperationMod
GLOBAL_REMOVE_IF_UNREFERENCED CONST UINT8  BnResultInverseMod[] =  {
  0x3a, 0xeb, 0xc5, 0x98, 0x9c, 0x22, 0xd6, 0x76, 0x7d, 0x1c, 0xc6, 0xd6, 0xbb, 0x1b, 0xed, 0xfd,
  0x0f, 0x34, 0xbf, 0xe0, 0x2b, 0x4a, 0x26, 0xc3, 0xc0, 0xd9, 0x57, 0xc7, 0x11, 0xc0, 0xd6, 0x35
};

// BnOperationA % BnOperationMod
GLOBAL_REMOVE_IF_UNREFERENCED CONST UINT8  BnResultExpMod[] =  {
  0x39, 0xf8, 0x74, 0xa0, 0xe8, 0x02, 0x8b, 0xf2, 0x22, 0x62, 0x82, 0x4c, 0xe0, 0xed, 0x63, 0x48,
  0xb9, 0xa2, 0xaa, 0xbc, 0xba, 0xb1, 0xd3, 0x6a, 0x02, 0xfd, 0xf3, 0x0e, 0x3a, 0x19, 0x39, 0x37
};

// BnOperationA >> 128
GLOBAL_REMOVE_IF_UNREFERENCED CONST UINT8  BnResultRShift[] =  {
  0x93, 0x61, 0x7a, 0xba, 0xcc, 0x41, 0x73, 0x49, 0xae, 0x20, 0x41, 0x31,
  0x12, 0xe6, 0xfa, 0x4e, 0x89, 0xa9, 0x7e, 0xa2, 0x0a, 0x9e, 0xee, 0xe6,0x4b,  0x55, 0xd3, 0x9a,
  0x21, 0x92, 0x99, 0x2a, 0x27, 0x4f, 0xc1, 0xa8, 0x36, 0xba, 0x3c, 0x23,0xa3,  0xfe, 0xeb, 0xbd
};

// 0x12345678
GLOBAL_REMOVE_IF_UNREFERENCED CONST UINT8  BnResultUIntSet[] =  { 0x12, 0x34, 0x56, 0x78 };

typedef struct {
  VOID    *BnA;
  VOID    *BnB;
  VOID    *BnC;
  VOID    *BnD;
  VOID    *BnCTX;
} BN_TEST_CONTEXT;

GLOBAL_REMOVE_IF_UNREFERENCED STATIC BN_TEST_CONTEXT  mBnContext = { NULL, NULL, NULL, NULL, NULL };

//
// Debug function
//
STATIC
BOOLEAN
EqualBn2Bn (
  CONST VOID  *Expected,
  CONST VOID  *Actual
  )
{
  if (BigNumCmp (Expected, Actual) == 0) {
    return TRUE;
  }

  return FALSE;
}

STATIC
BOOLEAN
EqualBn2Bin (
  CONST VOID   *Bn,
  CONST UINT8  *Buffer,
  CONST UINTN  BufferSize
  )
{
  UINTN  BnTestBufferSize;
  UINT8  BnTestBuffer[MAX_TEST_DATA_SIZE];

  BnTestBufferSize = BigNumToBin (Bn, BnTestBuffer);
  if (BnTestBufferSize == BufferSize) {
    if (CompareMem (Buffer, BnTestBuffer, BnTestBufferSize) == 0) {
      return TRUE;
    }
  }

  return FALSE;
}

UNIT_TEST_STATUS
EFIAPI
TestVerifyBnPreReq (
  UNIT_TEST_CONTEXT  Context
  )
{
  BN_TEST_CONTEXT  *BnContext;

  // MU_CHANGE [START]
  if (!PcdGetBool (PcdCryptoServiceBigNumInit) || !PcdGetBool (PcdCryptoServiceBigNumNewContext)) {
    return UNIT_TEST_ERROR_PREREQUISITE_NOT_MET;
  }

  // MU_CHANGE [END]

  BnContext        = Context;
  BnContext->BnCTX = BigNumNewContext ();
  BnContext->BnA   = BigNumInit ();
  BnContext->BnB   = BigNumInit ();
  BnContext->BnC   = BigNumInit ();
  BnContext->BnD   = BigNumInit ();
  if (  (BnContext->BnCTX == NULL)
     || (BnContext->BnA == NULL)
     || (BnContext->BnB == NULL)
     || (BnContext->BnC == NULL)
     || (BnContext->BnD == NULL)
        )
  {
    return UNIT_TEST_ERROR_TEST_FAILED;
  }

  return UNIT_TEST_PASSED;
}

VOID
EFIAPI
TestVerifyBnCleanUp (
  UNIT_TEST_CONTEXT  Context
  )
{
  BN_TEST_CONTEXT  *BnContext;

  BnContext = Context;
  BigNumContextFree (BnContext->BnCTX);
  BigNumFree (BnContext->BnA, TRUE);
  BigNumFree (BnContext->BnB, TRUE);
  BigNumFree (BnContext->BnC, TRUE);
  BigNumFree (BnContext->BnD, TRUE);
}

UNIT_TEST_STATUS
EFIAPI
TestVerifyBn (
  IN UNIT_TEST_CONTEXT  Context
  )
{
  BN_TEST_CONTEXT  *BnContext;
  UINTN            Num;

  // CONST VOID       *BnOne;  // MU_CHANGE

  BnContext = Context;

  // MU_CHANGE [START]
  if (!PcdGetBool (PcdCryptoServiceBigNumFromBin) || !PcdGetBool (PcdCryptoServiceBigNumIsWord) || !PcdGetBool (PcdCryptoServiceBigNumIsOdd) || !PcdGetBool (PcdCryptoServiceBigNumConstTime) || !PcdGetBool (PcdCryptoServiceBigNumBytes)) {
    return UNIT_TEST_ERROR_PREREQUISITE_NOT_MET;
  }

  // MU_CHANGE [END]

  // Calculation tests
  BnContext->BnA = BigNumFromBin (BnOperationA, sizeof (BnOperationA));
  BnContext->BnB = BigNumFromBin (BnOperationB, sizeof (BnOperationB));
  // C=A+B
  BigNumAdd (BnContext->BnA, BnContext->BnB, BnContext->BnC);
  UT_ASSERT_TRUE (EqualBn2Bin (BnContext->BnC, BnResultSum, sizeof (BnResultSum)));
  // D=C-A=B
  BigNumSub (BnContext->BnC, BnContext->BnA, BnContext->BnD);
  UT_ASSERT_TRUE (EqualBn2Bn (BnContext->BnB, BnContext->BnD));
  // C=(A+B)%D
  BnContext->BnD = BigNumFromBin (BnOperationMod, sizeof (BnOperationMod));
  BigNumAddMod (BnContext->BnA, BnContext->BnB, BnContext->BnD, BnContext->BnC);
  UT_ASSERT_TRUE (EqualBn2Bin (BnContext->BnC, BnResultSumMod, sizeof (BnResultSumMod)));
  // C=(A*B)%D
  BigNumMulMod (BnContext->BnA, BnContext->BnB, BnContext->BnD, BnContext->BnC);
  UT_ASSERT_TRUE (EqualBn2Bin (BnContext->BnC, BnResultMulMod, sizeof (BnResultMulMod)));
  // C=A/D
  BigNumDiv (BnContext->BnA, BnContext->BnD, BnContext->BnC);
  UT_ASSERT_TRUE (EqualBn2Bin (BnContext->BnC, BnResultDiv, sizeof (BnResultDiv)));
  // C=A%D
  BigNumMod (BnContext->BnA, BnContext->BnD, BnContext->BnC);
  UT_ASSERT_TRUE (EqualBn2Bin (BnContext->BnC, BnResultMod, sizeof (BnResultMod)));
  // 1=(A*C)%D
  BigNumInverseMod (BnContext->BnA, BnContext->BnD, BnContext->BnC);
  UT_ASSERT_TRUE (EqualBn2Bin (BnContext->BnC, BnResultInverseMod, sizeof (BnResultInverseMod)));
  // C=(A^B)%D
  BnContext->BnB = BigNumFromBin (BnOperationExp, sizeof (BnOperationExp));
  BigNumExpMod (BnContext->BnA, BnContext->BnB, BnContext->BnD, BnContext->BnC);
  UT_ASSERT_TRUE (EqualBn2Bin (BnContext->BnC, BnResultExpMod, sizeof (BnResultExpMod)));
  // C=A>>128
  BigNumRShift (BnContext->BnA, 128, BnContext->BnC);
  UT_ASSERT_TRUE (EqualBn2Bin (BnContext->BnC, BnResultRShift, sizeof (BnResultRShift)));
  // C=0x12345678
  BigNumSetUint (BnContext->BnC, 0x12345678);
  UT_ASSERT_TRUE (EqualBn2Bin (BnContext->BnC, BnResultUIntSet, sizeof (BnResultUIntSet)));
  // Bn compare
  UT_ASSERT_TRUE (BigNumIsWord (BnContext->BnC, 0x12345678));
  UT_ASSERT_FALSE (BigNumIsWord (BnContext->BnC, 0x12345600));
  UT_ASSERT_FALSE (BigNumIsOdd (BnContext->BnC));
  UT_ASSERT_TRUE (BigNumIsOdd (BnContext->BnA));

  // Other tests
  BigNumConstTime (BnContext->BnA);
  Num = BigNumBytes (BnContext->BnA);
  UT_ASSERT_EQUAL (Num, BYTES_OF_OPERATION_A);
  Num = BigNumBits (BnContext->BnA);
  UT_ASSERT_EQUAL (Num, BITS_OF_OPERATION_A);
  // MU_CHANGE [START] - Remove test for unused function

  /*BnOne = BigNumValueOne ();
  if (BnOne == NULL) {
    return UNIT_TEST_ERROR_TEST_FAILED;
  }*/

  // UT_ASSERT_TRUE (BigNumIsWord (BnOne, 0x1));
  // MU_CHANGE [END]

  return UNIT_TEST_PASSED;
}

TEST_DESC  mBnTest[] = {
  //
  // -----Description----------------Class---------------------Function-----------Pre----------------Post---------Context
  //
  { "TestVerifyBn()", "CryptoPkg.BaseCryptLib.BigNumber", TestVerifyBn, TestVerifyBnPreReq, TestVerifyBnCleanUp, &mBnContext },
};

UINTN  mBnTestNum = ARRAY_SIZE (mBnTest);
