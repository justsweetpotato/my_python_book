#!/usr/bin/env python
import re
from random import choice
from time import ctime
import os
from func_timeout.exceptions import FunctionTimedOut

from .number import pn, calc

URL = 'littlepotato.life'

def fake_ai(msg):
    yes_or_no = ['是', '不是!']
    answer = ['我不知道你在说什么', '我无法回答你的问题', '这是什么?']
    error = ['大兄弟, 想干啥?', '找打!', '喵喵喵???']

    if re.match('(你好|晚上好|早上好)$', msg):
        return '你好, 很高兴见到你!'
    if re.match('(日期|时间|date)$', msg):
        return ctime()
    if re.match('(再见|[Bb]ye|BYE)$', msg):
        return '好的, 祝你有个愉快的一天'
    if re.match('(谢谢|谢谢你|[Tt]hanks|THANKS|[Tt]hank you.?)$', msg):
        return '不客气哦'
    if (re.match('([Hh]i|HI|[Hh]ello|HELLO)$', msg)):
        return 'Hi, how are you?'
    if re.search('是不是', msg):
        return choice(yes_or_no)
    if re.search('.*?你.*?吗[\?\？]?', msg):
        msg = re.sub('你', '我', msg)
        return msg.strip('吗?？') + '!'
    elif re.search('我', msg):
        msg = re.sub('我', '你', msg)
        return msg.strip('吗?？') + '!'
    elif re.search('吗', msg):
        return msg.strip('吗?？') + '!'
    if re.match(r'.{1,3}[\?\？]', msg):
        return msg.strip('?？') + '!'
    if re.search('[好真太]', msg):
        return '谢谢!'
    if re.match('(pwd)$', msg):
        return os.getcwd()
    if re.match('(ls|ll)', msg):
        return os.listdir(os.getcwd())
    if re.search('(翻墙|科学上网)', msg):
        return "https://{}/451/".format(URL)
    if re.match('([Ll]ucy)$', msg):
        return '你好, 我能为你做些什么?'
    if re.match('(语雀)$', msg):
        return 'https://www.yuque.com/sweetpotato-u4hvd/python'
    if re.match('pn \d+', msg):
        try:
            msg = msg.split('pn ')[1]
            ans = pn(msg)
        except:
            ans = "参数不正确!"
        return ans
    if re.match('calc .*?', msg):
        msg = msg.split('calc ')[1]
        try:
            ans = calc(msg)
        except FunctionTimedOut as e:
            return "抓住你了!"
        if ans == 'error':
            return choice(error)
        return ans
    if re.match('eval', msg):
        return "拒绝访问! 权限认证失败."
    if re.match('crypto?', msg):
        return "https://{}/crypto_lv2/".format(URL)
    if re.match('(匿名|[Hh]idden])$', msg):
        return 'https://sweetpotato.xyz/hidden/'
    if re.match("(敏感词|64|谈笑风生|螳臂[当挡]车|8964)$", msg):
        return "https://{}/filter/".format(URL)
    else:
        return choice(answer)
