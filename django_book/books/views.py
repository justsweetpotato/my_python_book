# /usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

from .forms import BookForm, CryptoForm
from .ai import fake_ai
from .word import word, read_site, hidden_site, random_index_html
from .crypto import getRandomKey, MonoAlphabeticCipher
from .crypto2 import encrypt_oracle, decrypt_oralce
from .ftp import show_files_info


def index(request):
    msg = word()
    content = {'msg': msg}
    index_html = random_index_html()
    return render(request, index_html, content)


def study(request):
    content = read_site()
    return render(request, 'study.html', content)


def info(request):
    return render(request, 'info.html')


def live(request):
    return render(request, 'live.html')


def why(request):
    return render(request, 'why.html')


def test(request):
    content = {
        'text0': request.META['CONTENT_LENGTH'],
        'text1': request.META['CONTENT_TYPE'],
        'text2': request.META['HTTP_ACCEPT'],
        'text3': request.META['HTTP_ACCEPT_ENCODING'],
        'text4': request.META['HTTP_ACCEPT_LANGUAGE'],
        'text5': request.META['HTTP_HOST'],
        'text6': request.META['HTTP_USER_AGENT'],
        'text7': request.META['QUERY_STRING'],
        'text8': request.META['REMOTE_ADDR'],
        'text9': request.META['REMOTE_HOST'],
        'text10': request.META['REQUEST_METHOD'],
        'text11': request.META['SERVER_NAME'],
        'text12': request.META['SERVER_PORT'],
    }
    return render(request, 'test.html', content)


def f451(request):
    return render(request, './../../django_book/templates/451.html', status=451)


def bigbrother(request):
    content = hidden_site()
    return render(request, 'bigbrother.html', content)


def bbs(request):
    return render(request, 'bbs.html')


def ai(request):
    if request.method != 'POST':
        form = BookForm()
        return render(request, 'ai.html', {'form': form})
    else:
        form = BookForm(request.POST)
        if form.is_valid():  # 验证表单数据
            msg = form.cleaned_data['text']  # 获取验证后的表单数据
            f = fake_ai(msg)
            content = {'f': f, 'msg': msg}
            return render(request, 'ai.html', content)
        else:
            return render(request, 'ai.html', {'form': form})


def crypto(request):
    if request.method != 'POST':
        return render(request, 'crypto.html')
    else:
        form = CryptoForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            c_key = form.cleaned_data['key']
            mode = 'encrypt'
            eptext = MonoAlphabeticCipher(c_key, text, mode).get('translated')
            if eptext:
                content = {'eptext': eptext}
            else:
                text = "不正确的密钥！"
                content = {'c_key_error': text}
            return render(request, 'crypto.html', content)
        else:
            text = "不允许为空!"
            content = {'error': text}
            return render(request, 'crypto.html', content)


def decrypto(request):
    if request.method != 'POST':
        return render(request, 'crypto.html')
    else:
        form = CryptoForm(request.POST)
        if form.is_valid():
            eptext = form.cleaned_data['text']
            c_key = form.cleaned_data['key']
            mode = 'decrypt'
            text = MonoAlphabeticCipher(c_key, eptext, mode).get('translated')
            if text:
                content = {'text': text}
            else:
                text = '不正确的密钥！'
                content = {'key_error': text}
            return render(request, 'crypto.html', content)

        else:
            text = "不允许为空！"
            content = {'d_error': text}
            return render(request, 'crypto.html', content)


def get_key(request):
    if request.method != 'POST':
        key = getRandomKey()
        content = {'key': key}
        return render(request, 'crypto.html', content)


def crypto_lv2(request):
    if request.method != 'POST':
        return render(request, 'crypto2.html')
    else:
        form = CryptoForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']  # 获取密文
            key = form.cleaned_data['key']  # 获取密钥
            crypto_text = form.cleaned_data['crypto_text']  # 获取密文

            if text and key:  # 如果存在明文和密钥, 则做加密, 如果三者都存在优先做加密
                serverMsg = encrypt_oracle(key, text).get('translated')
                if serverMsg:  # 密钥正确返回密文
                    content = {'serverMsgCT': serverMsg}
                else:  # 密钥错误, 返回空字典
                    content = {'error': '密钥不正确!'}

            elif crypto_text and key:  # 如果存在密文和明文, 则做解密
                serverMsg = decrypt_oralce(key, crypto_text).get('translated')
                if serverMsg:
                    content = {'serverMsgT': serverMsg}
                else:
                    content = {'error': '密钥不正确!'}

            else:  # 其他情况, 只输入了密钥, 返回错误信息
                content = {'error': '缺少明文或密文!'}
            return render(request, 'crypto2.html', content)

        else:  # 验证失败
            text = "密钥为空! 或长度超出限制!"
            content = {'error': text}
            return render(request, 'crypto2.html', content)


def hidden(request):
    return render(request, 'hidden.html')


def filter(request):
    return render(request, 'filter.html')


def hello(request):
    return HttpResponse("Congratulations!<br>You found this!<br><br>The answer is <b>42</b>.<br>")


def dark(request):
    return render(request, 'dark.html')


def ftp(request):
    content = show_files_info()
    return render(request, 'ftp.html', content)


def page404(request):
    # return render(request, "./../../django_book/templates/404.html")
    return render(request, "404.html")


def youtube(request):
    return render(request, "youtube.html")


def attack(request):
    return render(request, 'attack.html')


def mirror(request):
    content = (
        ('www.google.com', 'go.littlepotato.life', 'WorkersProxy'),
        ('zh.wikipedia.org', 'wiki.littlepotato.life', 'WorkersProxy'),
        ('www.youtube.com', 'bot-yt-1.herokuapp.com', 'You2Php'),
        ('drive.google.com', 'drive.littlepotato.life', 'GoIndex'),
    )

    return render(request, 'mirror.html', {'content': content})
