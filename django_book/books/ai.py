#!/usr/bin/env python
import re
from random import choice
from time import ctime
import os

from .number import pn, calc


def fake_ai(msg):
    yes_or_no = ['是', '不是!']
    answer = ['我不知道你在说什么', '我无法回答你的问题', '这是什么?']
    error = ['大兄弟, 想干啥?', '找打!', '喵喵喵???']

    if (msg == '你好') or ('晚上好' in msg) or ('早上好' in msg):
        return '你好, 很高兴见到你!'
    elif (msg == '日期') or (msg == '时间') or (msg == 'date'):
        return ctime()
    elif ('再见' in msg) or ('bye' in msg):
        return '好的, 祝你有个愉快的一天'
    elif ('谢谢' in msg) or ('谢谢你' in msg):
        return '不客气哦'
    elif ('hi' in msg) or ('hello' in msg):
        return 'hi'
    elif '是不是' in msg:
        return choice(yes_or_no)
    elif ('你' in msg) and ('吗' in msg):
        msg = re.sub('你', '我', msg)
        return msg.strip('吗?？') + '!'
    elif '我' in msg:
        msg = re.sub('我', '你', msg)
        return msg.strip('吗?？') + '!'
    elif '吗' in msg:
        return msg.strip('吗?？') + '!'
    elif re.match(r'.{1,3}[\?\？]', msg):
        return msg.strip('?？') + '!'
    elif ('好' in msg) or ('真' in msg) or ('太' in msg):
        return '谢谢!'
    elif msg == 'pwd':
        return os.getcwd()
    elif msg == 'ls':
        return os.listdir(os.getcwd())
    elif msg == '翻墙':
        return "https://sweetpotato.xyz/1984/"
    elif msg == 'lucy':
        return '你好, 我能为你做些什么?'
    elif msg == '语雀':
        return 'https://www.yuque.com/sweetpotato-u4hvd/python'
    elif 'pn' in msg:  # TODO: 逻辑可改进
        try:
            msg = msg.split('pn ')[1]
            ans = pn(msg)
        except:
            ans = "参数不正确!"
        return ans
    elif 'calc' in msg:
        msg = msg.split('calc ')[1]
        if ('__import__' in msg) or ('open' in msg) or ('os' in msg) or ('rm' in msg):
            return choice(error)
        ans = calc(msg)
        return ans
    elif 'eval' in msg:
        return "拒绝! 权限认证失败."
    elif msg == 'crypto':
        return "https://sweetpotato.xyz/crypto_lv2/"
    elif msg == '匿名':
        return 'https://sweetpotato.xyz/hidden/'
    else:
        return choice(answer)


if __name__ == '__main__':
    print('你好, 我是 Lucy.')
    while True:
        msg = input()
        f = fake_ai(msg)
        print(f)
        if (msg == '再见') or (msg == 'bye'):
            break
