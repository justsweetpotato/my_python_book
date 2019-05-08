#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def show_dir_files():
    # 返回当前目录下所有文件和大小
    files = os.listdir('../static/pdf/share')
    files_size_list = []
    for file_name in files:
        file_path = '../static/pdf/share/{}'.format(file_name)
        file_size = os.path.getsize(file_path)
        file_size = file_size / 1024
        if file_size >= 1000:
            file_size = file_size / 1024
            if file_size >= 1000:
                file_size = file_size / 1024
                file_size = "{:>7.2f} {}".format(file_size, "GB")
            else:
                file_size = "{:>7.2f} {}".format(file_size, "MB")
        else:
            file_size = "{:>7.2f} {}".format(file_size, "KB")
        files_size_list.append(file_size)
    content = {"content": dict(zip(files, files_size_list))}

    return content
