# -*- coding: utf-8 -*-
# @Time    : 2021/10/6 12:35
# @Author  : B612
# @File    : 04-sub.py

import re

"""
    re.sub(pattern, repl, string[,count  ,flag])
    # count 是最多替换的次数
    # 不指定就是全部替换
"""
str = "NO.1 No.2 No.3"

pat = re.compile("(no)", re.M | re.I)
print(pat.sub("num", str, 2))  # 替换两次

