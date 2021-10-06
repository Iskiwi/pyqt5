# -*- coding: utf-8 -*-
# @Time    : 2021/10/6 14:38
# @Author  : B612
# @File    : 06-escape.py

import re

"""
    将字符串中正则表达式特殊字符之前加上转义符 “\”，  再返回
"""
print(re.escape("www.python.org"))

# result： www\.python\.org