#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
from time import localtime, strftime

SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}


def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    '''Convert a file size to human-readable form.
    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000
    Returns: string
    '''
    if size < 0:
        raise ValueError('number must be non-negative')

    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000

    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('number too large')


def show_files_info():
    # 返回当前目录下所有文件的 文件名, 修改时间, 文件大小
    files = glob.glob("../static/pdf/share/*")
    # files_name = os.listdir('../static/pdf/share')
    files_name = []
    files_atime = []
    files_size = []

    for file in files:
        files_name.append(os.path.split(file)[-1])
        files_atime.append(strftime('%Y-%m-%d %H:%M:%S', localtime(os.stat(file).st_atime)))
        files_size.append(approximate_size(os.stat(file).st_size))
    content = {"content": zip(files_name, files_atime, files_size)}

    return content
