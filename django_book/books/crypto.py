#!/usr/bin/env python

import random
import base64

LETTERS = 'vLEWA3J6jiFMGk+cfwhe7gtoKr2Pa/TmbH=u5npRlQ49d1x0ICDqsVBONSXZzU8Yy'


def getRandomKey():  # 得到随机密钥
    key = list(LETTERS)
    random.shuffle(key)
    key = ''.join(key)
    return key


def checkValidKey(key):  # 验证密钥
    '''这一段主要是检查密钥是否正确,如果不正确输出错误提示,然后sys.exit终止程序'''
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList == lettersList:
        return "pass"


def MonoAlphabeticCipher(key, message, mode):  # 加密解密函数
    '''
    LETTERS里面26个字母如果在材料(message)里面出现 则替换密钥相同位置的字母
    :param key: 密钥
    :param message: 明文
    :param mode: 当mode=encrypt的时候加密, mode=decrypt的时候则为解密
    :return:
    '''
    assert isinstance(message, str), "message类型错误"

    # message = message.replace('\n', '')  # 删除材料中的换行符
    if not checkValidKey(key):  # 检查密钥
        return {}
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'encrypt':
        message = message.encode()
        message = base64.b64encode(message)
        message = message.decode()

        for symbol in message:
            assert symbol in charsA, "base64字符串错误"
            symIndex = charsA.find(symbol)  # 返回当前字符的索引
            translated += charsB[symIndex]

    elif mode == 'decrypt':
        charsA, charsB = charsB, charsA
        for symbol in message:
            assert symbol in charsA, "base64字符串错误"
            symIndex = charsA.find(symbol)  # 返回当前字符的索引
            translated += charsB[symIndex]
        translated = translated.encode()
        translated = base64.b64decode(translated)
        translated = translated.decode()
    else:
        raise ValueError("缺少参数 mode")

    return {'translated': translated}
