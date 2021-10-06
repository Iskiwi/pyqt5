# -*- coding: utf-8 -*-
# @Time    : 2021/10/6 14:48
# @Author  : B612
# @File    : 01-异常的正常捕捉.py

import random
try:
    # a = 1/0
    res = random.randint(1, 5)
    print(res)
except:
    print("代码出错了， 我们这么做")
else:
    print("代码没问题， 我就执行")
finally:
    print("wo!")




