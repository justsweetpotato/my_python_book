#!/usr/bin/env python
import base64
from Crypto.Cipher import AES

'''
采用AES对称加密算法
'''


# str不是16的倍数那就补足为16的倍数
def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes


# 加密方法
def encrypt_oracle(key, text):
    text = base64.b64encode(text.encode()).decode()
    try:
        # 初始化加密器
        aes = AES.new(add_to_16(key), AES.MODE_ECB)
        # 先进行aes加密
        encrypt_aes = aes.encrypt(add_to_16(text))
    except:
        encrypted_text = {}
    else:
        # 用base64转成字符串形式
        encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码返回str
    return {'translated': encrypted_text}


# 解密方法
def decrypt_oralce(key, text):
    try:
        # 初始化加密器
        aes = AES.new(add_to_16(key), AES.MODE_ECB)
        # 优先逆向解密base64成bytes
        base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))
        # 执行解密密并转码返回str
        decrypted_text = str(aes.decrypt(base64_decrypted), encoding='utf-8').replace('\0', '')
    except:
        decrypted_text = {}
    else:
        decrypted_text = base64.b64decode(decrypted_text.encode()).decode()
    return {'translated': decrypted_text}


if __name__ == '__main__':
    key = '哈哈哈'
    text = 'abcdefg'
    text = encrypt_oracle(key, text)
    print(text)
    key = '哈哈哈'
    text = 'ZpUEjy8TPhnV06nUxGMrZg=='
    print(decrypt_oralce(key, text)['translated'])
