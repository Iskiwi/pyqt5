# -*- coding: utf-8 -*-
# @Time    : 2021/10/6 15:10
# @Author  : B612
# @File    : 03-断言处理.py

a, b = eval(input())
assert b != 0, "除数不能为零"
c = a/b
print(a, "/", b, "=", c)

