"""
Author: pyhanker
Email: pyhanker@gmail.com
Date: 2024-01-16


This code is provided as-is, without any warranty.
You can modify and use it for your own purposes.
"""
import codecs
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
from Crypto.Random import get_random_bytes


def aes_encrypt(plaintext: str, key: bytes) -> bytes:
    """
    Encrypts the given plaintext using the given key.
    """
    iv = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return iv + ciphertext


def aes_decrypt(ciphertext: bytes, key: bytes) -> str:
    """
    Decrypts the given ciphertext using the given key.
    """
    ciphertext = codecs.escape_decode(ciphertext, 'hes-escape')[0]
    iv = ciphertext[:AES.block_size]
    ciphertext = ciphertext[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode()


if __name__ == '__main__':
    secret_key = b'mHAxsLYzemss2024'
    order = input("Insert order num:\n1. Encrypt\n2. Decrypt\n")
    assert order in ['1', '2'], "Only support 1 or 2"

    if order == '1':
        plaintext = input("Please input plaintext password:\n")
        encrypted = aes_encrypt(plaintext, secret_key)
        print("Encrypt result:\n", encrypted)
    elif order == '2':
        ciphertext = input("Please input ciphertext password:\n")
        decrypted = aes_decrypt(ciphertext, secret_key)
        print("Decrypt result:\n", decrypted)
    else:
        print("Not supported")