# -*- coding: utf-8 -*-
# @Time    : 2021/10/6 16:35
# @Author  : B612
# @File    : 04-异常和保证文件关闭.py

try:
    fl = open("test.txt", "w")
    while True:
        s = input()
        if s.upper() == "Q":
            break
        fl.write(s)
except KeyboardInterrupt as K:
    print("出错了", K)

finally:
    print("正在关闭test文件")
    fl.close()
