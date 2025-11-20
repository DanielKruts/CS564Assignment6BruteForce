import sys
import itertools
import string
from BitVector import *

# ===============================================================
# Final brute-force script for Avi Kak's EncryptForFun assignment
# BLOCKSIZE = 16 bits (DO NOT CHANGE)
# Keyspace = all 2-character strings of letters + digits (3844 keys)
# ===============================================================

PassPhrase = "Hopes and dreams of a million years"
BLOCKSIZE = 16             # 16 bits
numbytes = BLOCKSIZE // 8  # 2 bytes

# Build IV exactly like DecryptForFun.py
def build_iv():
    bv_iv = BitVector(bitlist=[0] * BLOCKSIZE)
    for i in range(0, len(PassPhrase) // numbytes):
        textstr = PassPhrase[i*numbytes:(i+1)*numbytes]
        bv_iv ^= BitVector(textstring=textstr)
    return bv_iv

# Key reduction exactly as in DecryptForFun.py
def reduce_key(key):
    key_bv = BitVector(bitlist=[0] * BLOCKSIZE)
    for i in range(0, len(key) // numbytes):
        keyblock = key[i*numbytes:(i+1)*numbytes]
        key_bv ^= BitVector(textstring=keyblock)
    return key_bv

# Decrypt using a candidate key
def decrypt_attempt(cipher_bv, key):
    iv = build_iv()
    key_bv = reduce_key(key)

    msg_bv = BitVector(size=0)
    prev = iv

    for i in range(0, len(cipher_bv) // BLOCKSIZE):
        bv = cipher_bv[i*BLOCKSIZE:(i+1)*BLOCKSIZE]
        temp = bv.deep_copy()
        bv ^= prev
        prev = temp
        bv ^= key_bv
        msg_bv += bv

    try:
        plaintext = msg_bv.get_text_from_bitvector()
        return plaintext
    except UnicodeDecodeError:
        return None

def main():
    known_plaintext = open("plain.txt").read().strip()
    # Used for comparison of the decrypted text to see if it generally matches, 64 characters in should be enough to determine correctness
    CHECK_LEN = 64  
    expected = known_plaintext[:CHECK_LEN]
    # Load encrypted hex
    cipher_hex = open("encrypted.txt").read().strip()

    cipher_bv = BitVector(hexstring=cipher_hex)

    # Build keyspace
    chars = string.ascii_letters + string.digits
    keyspace = (''.join(p) for p in itertools.product(chars, repeat=2))

    print("[*] Starting brute-force search over 3844 keys...")

    for key in keyspace:
        decrypted = decrypt_attempt(cipher_bv, key)
        if decrypted is None:
            continue

        if decrypted[:CHECK_LEN] == expected:
            print("\n[+] Found likely key:", key)

            print("[+] Decrypted text: ", decrypted)
            return

    print("[-] No key found (this should NOT happen).")

if __name__ == "__main__":
    main()
