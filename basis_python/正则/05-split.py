# -*- coding: utf-8 -*-
# @Time    : 2021/10/6 14:26
# @Author  : B612
# @File    : 05-split.py

import re

"""
    re.split(patter, string[,maxsplit  ,flag])
"""

p = re.compile(r"\W+")
print(p.split("192.168.1.1"))
print(re.split(r'(\W+)', "192.168.1.1"))
print(re.split(r'(\W+)', "192.168.1.1", 1))

# 分割匹配的pattern 是分割的依据
print(re.split("\.", "192.168.1.1"))  # ['192', '168', '1', '1']


