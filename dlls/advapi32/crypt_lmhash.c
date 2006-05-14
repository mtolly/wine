/*
 *  Copyright 2004 Hans Leidekker
 *
 *  Based on LMHash.c from libcifs
 *
 *  Copyright (C) 2004 by Christopher R. Hertel
 *
 *  This library is free software; you can redistribute it and/or
 *  modify it under the terms of the GNU Lesser General Public
 *  License as published by the Free Software Foundation; either
 *  version 2.1 of the License, or (at your option) any later version.
 *
 *  This library is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 *  Lesser General Public License for more details.
 *
 *  You should have received a copy of the GNU Lesser General Public
 *  License along with this library; if not, write to the Free Software
 *  Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 */

#include <stdarg.h>

#include "ntstatus.h"
#define WIN32_NO_STATUS
#include "windef.h"
#include "winbase.h"
#include "winreg.h"
#include "winternl.h"

#include "crypt.h"

static const unsigned char CRYPT_LMhash_Magic[8] =
    { 'K', 'G', 'S', '!', '@', '#', '$', '%' };

static void CRYPT_LMhash( unsigned char *dst, const unsigned char *pwd, const int len )
{
    int i, max = 14;
    unsigned char tmp_pwd[14] = { 0,0,0,0,0,0,0,0,0,0,0,0,0,0 };

    max = len > max ? max : len;

    for (i = 0; i < max; i++)
        tmp_pwd[i] = pwd[i];

    CRYPT_DEShash( dst, tmp_pwd, CRYPT_LMhash_Magic );
    CRYPT_DEShash( &dst[8], &tmp_pwd[7], CRYPT_LMhash_Magic );
}

NTSTATUS WINAPI SystemFunction006( LPCSTR password, LPSTR hash )
{
    CRYPT_LMhash( (unsigned char*)hash, (unsigned char*)password, strlen(password) );

    return STATUS_SUCCESS;
}

/******************************************************************************
 * SystemFunction008  [ADVAPI32.@]
 *
 * Creates a LM response from a challenge and a password hash
 *
 * PARAMS
 *   challenge  [I] Challenge from authentication server
 *   hash       [I] NTLM hash (from SystemFunction006)
 *   response   [O] response to send back to the server
 *
 * RETURNS
 *  Success: STATUS_SUCCESS
 *  Failure: STATUS_UNSUCCESSFUL
 *
 * NOTES
 *  see http://davenport.sourceforge.net/ntlm.html#theLmResponse
 *
 */
NTSTATUS WINAPI SystemFunction008(const LPBYTE challenge, const LPBYTE hash, LPBYTE response)
{
    BYTE key[7*3];

    if (!challenge || !response)
        return STATUS_UNSUCCESSFUL;

    memset(key, 0, sizeof key);
    memcpy(key, hash, 0x10);

    CRYPT_DEShash(response, key, challenge);
    CRYPT_DEShash(response+8, key+7, challenge);
    CRYPT_DEShash(response+16, key+14, challenge);

    return STATUS_SUCCESS;
}

/******************************************************************************
 * SystemFunction001  [ADVAPI32.@]
 *
 * Encrypts a single block of data using DES
 *
 * PARAMS
 *   data    [I] data to encrypt    (8 bytes)
 *   key     [I] key data           (7 bytes)
 *   output  [O] the encrypted data (8 bytes)
 *
 * RETURNS
 *  Success: STATUS_SUCCESS
 *  Failure: STATUS_UNSUCCESSFUL
 *
 */
NTSTATUS WINAPI SystemFunction001(const LPBYTE data, const LPBYTE key, LPBYTE output)
{
    if (!data || !output)
        return STATUS_UNSUCCESSFUL;
    CRYPT_DEShash(output, key, data);
    return STATUS_SUCCESS;
}

/******************************************************************************
 * SystemFunction002  [ADVAPI32.@]
 *
 * Decrypts a single block of data using DES
 *
 * PARAMS
 *   data    [I] data to decrypt    (8 bytes)
 *   key     [I] key data           (7 bytes)
 *   output  [O] the decrypted data (8 bytes)
 *
 * RETURNS
 *  Success: STATUS_SUCCESS
 *  Failure: STATUS_UNSUCCESSFUL
 *
 */
NTSTATUS WINAPI SystemFunction002(const LPBYTE data, const LPBYTE key, LPBYTE output)
{
    if (!data || !output)
        return STATUS_UNSUCCESSFUL;
    CRYPT_DESunhash(output, key, data);
    return STATUS_SUCCESS;
}

/******************************************************************************
 * SystemFunction003  [ADVAPI32.@]
 *
 * Hashes a key using DES and a fixed datablock
 *
 * PARAMS
 *   key     [I] key data    (7 bytes)
 *   output  [O] hashed key  (8 bytes)
 *
 * RETURNS
 *  Success: STATUS_SUCCESS
 *  Failure: STATUS_UNSUCCESSFUL
 *
 */
NTSTATUS WINAPI SystemFunction003(const LPBYTE key, LPBYTE output)
{
    if (!output)
        return STATUS_UNSUCCESSFUL;
    CRYPT_DEShash(output, key, CRYPT_LMhash_Magic);
    return STATUS_SUCCESS;
}
