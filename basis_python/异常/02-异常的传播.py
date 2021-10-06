# -*- coding: utf-8 -*-
# @Time    : 2021/10/6 15:08
# @Author  : B612
# @File    : 02-异常的传播.py


"""
    函数中的异常未解决的话会向调用处传播
    若一直未解决，则当异常传播到全局作用域的时候
    自动报错，结束运行
"""


def fun1():
    print(1 / 0)  #


def fun2():
    fun1()  #


def fun3():
    fun2()  #


def fun4():
    fun3()  #


def fun5():
    fun4()  #


def fun6():
    fun5()  #


fun6()  #

# 共七处错误
