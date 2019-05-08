#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time


def show_dir_files():
    # 返回当前目录下所有文件和大小
    files = os.listdir('../static/pdf/share')
    t_list = get_FileModifyTime()
    files_size_list = get_FileSize()

    content = {"content": list(zip(files, t_list, files_size_list))}

    return content


def get_FileSize():
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

    return files_size_list


def get_FileModifyTime():
    files = os.listdir('../static/pdf/share')
    t_list = []

    for file_name in files:
        file_path = '../static/pdf/share/{}'.format(file_name)
        t = os.path.getmtime(file_path)
        t_list.append(t)

    return TimeStampToTime(t_list)


def TimeStampToTime(timestamp_list):
    timeStruct_list = []

    for timestamp in timestamp_list:
        timeStruct = time.localtime(timestamp)
        timeStruct = time.strftime('%Y-%m-%d', timeStruct)
        timeStruct_list.append(timeStruct)

    return timeStruct_list
