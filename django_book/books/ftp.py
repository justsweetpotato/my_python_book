#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def list_dir_files():
    files = os.listdir('../static/pdf/share')
    content = {'content': files}
    return content
