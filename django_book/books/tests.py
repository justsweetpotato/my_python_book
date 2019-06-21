# from django.test import TestCase
#
#
# # Create your tests here.
# def add_to_16(value):
#     while len(value) % 16 != 0:
#         value += '\0'
#     return str.encode(value)  # 返回bytes
#
#
# # print(add_to_16('11111111111111111'))
#
# def math(x):
#     if '**' in x:
#         ans = x.split("**")
#         if len(ans) > 2:
#             return "暂时仅支持单独的乘方运算."
#         for y in ans:
#             try:
#                 int(y)
#             except:
#                 return "暂时仅支持单独的乘方运算."
#             if len(str(y)) > 2:
#                 return "暂时仅支持2位数以内的乘方运算."
#
#     return eval(x)
#
#
# while True:
#     print(math(input(">")))

#
# import os
#
#
# def list_dir_files():
#     files = os.listdir('../static/pdf/share')
#     content = {'content': files}
#     print(content)
#     return content
from func_timeout import func_set_timeout
from func_timeout.exceptions import FunctionTimedOut
import time


@func_set_timeout(5)  # 函数执行多少秒后退出
def task():
    index = 1
    while True:
        print('{} hello world!'.format(index))
        time.sleep(1)
        index += 1


if __name__ == '__main__':
    try:
        task()
    except FunctionTimedOut as e:
        print("超时退出...", str(e))
