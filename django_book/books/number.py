#!/usr/bin/env python


def pn(x):
    # 求质数
    try:
        x = int(x)
    except ValueError:
        return "错误: 参数必须为整数!"
    else:
        try:
            assert x < 20000
        except AssertionError:
            return "输入值过大, 会引起性能问题. 暂时还不能这样哦!"

    start_num = 2  # 起始质数
    count_n = 0  # 索引计数器
    list_n = list(range(start_num, x + 1))  # 生成列表
    while True:
        for i in list_n[count_n:]:
            if i % start_num == 0 and i != start_num:  # 如果列表中有起始质数的倍数(不包括)则一定不是质数
                list_n.remove(i)
        count_n += 1  # 索引计数器 +1
        try:
            start_num = list_n[count_n]  # 起始质数变成列表中的下一个元素元素(第二次是第二个(3), 第三次是第三个(5), 类推)
        except IndexError:
            break  # 如果出现索引越界异常表示列表中最后一个已经是质数, 捕获异常并退出循环
    return list_n


def calc(x):
    # 计算器
    if '**' in x:
        ans = x.split("**")
        if len(ans) > 2:
            return "暂时仅支持单独的乘方运算."
        for y in ans:
            try:
                int(y)
            except:
                return "暂时仅支持单独的乘方运算."
            if len(str(y)) > 2:
                return "暂时仅支持2位数以内的乘方运算."
    return eval(x)
