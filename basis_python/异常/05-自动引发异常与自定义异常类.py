# -*- coding: utf-8 -*-
# @Time    : 2021/10/6 16:46
# @Author  : B612
# @File    : 05-自动引发异常与自定义异常类.py


class Errora(Exception):
    def __init__(self, data):
        self.data = data


def average(data):
    sum = 0
    for i in data:
        if i < 0:
            raise Errora("成绩不能为零")
        sum += i
    return sum/len(data)


def main():
    score = eval(input())
    print(average(score))


main()
