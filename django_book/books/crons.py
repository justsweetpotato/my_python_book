#!/usr/bin/env python
# -*- coding: utf-8 -*-
# heroku 应用激活(每小时, 对应设置在 settings 中.)

import requests


def keep_app1_alive():
    with requests.get("https://web--proxy.herokuapp.com/") as r:
        return


def keep_app2_alive():
    with requests.get("https://gogogo-google.herokuapp.com/") as r:
        return


def keep_app3_alive():
    with requests.get("https://search-books.herokuapp.com") as r:
        return
