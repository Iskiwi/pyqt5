# -*- coding: utf-8 -*-
# @Time    : 2021/10/5 18:38
# @Author  : B612
# @File    : 01-match.py

import re

"""
    https://blog.csdn.net/qq_20412595
    
    正则有两种匹配的方式：
    区别：是否生成了正则对象
    1、 不生成正则对象
    re.match(pattern, string[,flag])
    
    pattern: 匹配的正则表达式
    flag:  re.I  re.M
    
    
    2、生成对象
    re.compile(pattern[,flag]) 生成正则对象
    match(string[, pos[,endpos]])
"""

"""
    一|
"""
string = "hELlo world"
m = re.match(r"^[\w]{3}", string)
m = re.match(r"^[H][\w]{2}", string, re.I)
if m:
    print(m)  # <re.Match object; span=(0, 3), match='hEL'>
    # 在字符串中，寻找匹配的位置
    print(m.group())
else:
    pass
"""
    二|
"""
line = "Cats are smarter than dogs"
pattern = re.compile(r"^(.*) are (.*?) .*", re.M | re.I)
matchobject = pattern.match(line)
if matchobject:
    print(matchobject.group())
    print(matchobject.group(1))
    print(matchobject.group(2))

