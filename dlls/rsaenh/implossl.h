/*
 * dlls/rsaenh/implossl.h
 * Encapsulating the OpenSSL dependend parts of RSABASE
 *
 * Copyright (c) 2004 Michael Jung
 *
 * based on code by Mike McCormack and David Hammerton
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 */

#ifndef __WINE_IMPLOSSL_H
#define __WINE_IMPLOSSL_H

#ifdef HAVE_OPENSSL_MD2_H
#include <openssl/md2.h>
#endif 

#ifdef HAVE_OPENSSL_RC2_H
#include <openssl/rc2.h>
#endif

#ifdef HAVE_OPENSSL_RC4_H
#include <openssl/rc4.h>
#endif

#ifdef HAVE_OPENSSL_DES_H
#include <openssl/des.h>
#endif

#ifdef HAVE_OPENSSL_RSA_H
#include <openssl/rsa.h>
#endif

/* Next typedef copied from dlls/advapi32/crypt_md4.c */
typedef struct tagMD4_CTX {
    unsigned int buf[4];
    unsigned int i[2];
    unsigned char in[64];
    unsigned char digest[16];
} MD4_CTX;

/* Next typedef copied from dlls/advapi32/crypt_md5.c */
typedef struct tagMD5_CTX
{
    unsigned int i[2];
    unsigned int buf[4];
    unsigned char in[64];
    unsigned char digest[16];
} MD5_CTX;

/* Next typedef copied form dlls/advapi32/crypt_sha.c */
typedef struct tagSHA_CTX
{
    ULONG Unknown[6];
    ULONG State[5];
    ULONG Count[2];
    UCHAR Buffer[64];
} SHA_CTX, *PSHA_CTX;

typedef union tagHASH_CONTEXT {
#ifdef HAVE_OPENSSL_MD2_H
    MD2_CTX md2;
#endif
    MD4_CTX md4;
    MD5_CTX md5;
    SHA_CTX sha;
} HASH_CONTEXT;

typedef union tagKEY_CONTEXT {
#ifdef HAVE_OPENSSL_RC2_H
    RC2_KEY rc2;
#endif
#ifdef HAVE_OPENSSL_RC4_H
    RC4_KEY rc4;
#endif
#ifdef HAVE_OPENSSL_DES_H
    DES_key_schedule des[3];
#endif
#ifdef HAVE_OPENSSL_RSA_H
    RSA *rsa;
#endif
    DWORD dwDummy;
} KEY_CONTEXT;

BOOL load_lib(void);

BOOL init_hash_impl(ALG_ID aiAlgid, HASH_CONTEXT *pHashContext);
BOOL update_hash_impl(ALG_ID aiAlgid, HASH_CONTEXT *pHashContext, CONST BYTE *pbData, 
                      DWORD dwDataLen);
BOOL finalize_hash_impl(ALG_ID aiAlgid, HASH_CONTEXT *pHashContext, BYTE *pbHashValue);
BOOL duplicate_hash_impl(ALG_ID aiAlgid, CONST HASH_CONTEXT *pSrcHashContext, 
                         HASH_CONTEXT *pDestHashContext);

BOOL new_key_impl(ALG_ID aiAlgid, KEY_CONTEXT *pKeyContext, DWORD dwKeyLen);
BOOL free_key_impl(ALG_ID aiAlgid, KEY_CONTEXT *pKeyContext);
BOOL setup_key_impl(ALG_ID aiAlgid, KEY_CONTEXT *pKeyContext, DWORD dwKeyLen, DWORD dwSaltLen, 
                    BYTE *abKeyValue);
BOOL duplicate_key_impl(ALG_ID aiAlgid, CONST KEY_CONTEXT *pSrcKeyContext, 
                        KEY_CONTEXT *pDestKeyContext);

BOOL encrypt_block_impl(ALG_ID aiAlgid, KEY_CONTEXT *pKeyContext, CONST BYTE *pbIn, BYTE *pbOut, 
                        DWORD enc);
BOOL encrypt_stream_impl(ALG_ID aiAlgid, KEY_CONTEXT *pKeyContext, BYTE *pbInOut, DWORD dwLen);

BOOL export_public_key_impl(BYTE *pbDest, KEY_CONTEXT *pKeyContext, DWORD dwKeyLen, 
                            DWORD *pdwPubExp);
BOOL import_public_key_impl(CONST BYTE *pbSrc, KEY_CONTEXT *pKeyContext, DWORD dwKeyLen, 
                            DWORD dwPubExp);
BOOL export_private_key_impl(BYTE *pbDest, KEY_CONTEXT *pKeyContext, DWORD dwKeyLen, 
                             DWORD *pdwPubExp);
BOOL import_private_key_impl(CONST BYTE* pbSrc, KEY_CONTEXT *pKeyContext, DWORD dwKeyLen, 
                             DWORD dwPubExp);

BOOL gen_rand_impl(BYTE *pbBuffer, DWORD dwLen);

#endif /* __WINE_IMPLOSSL_H */
