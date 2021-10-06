# -*- coding: utf-8 -*-
# @Time    : 2021/10/6 12:26
# @Author  : B612
# @File    : 03-findall.py

import re

str1 = "www.baidu.com"
str2 = "www.baidu.com www.baidu.edu.com"
pat = r"[w]{3}\.([a-zA-Z]+\.)+com"

print(re.findall(pat, str1))
print(re.findall(pat, str2))

str = "<h1>liuwei</h1><a href='www.baidu.com'></a><h1>zhangbin</h1><a href='www.love.com'></a>"


# 分析 ：要获取h标签里的 title 和 a 标签里的链接
# 1、分成两部分
# 2、findall 获取全部子串
# 3、 （） 作为整体 group（）获取
pat = "<h1>([a-zA-Z]+)</h1><a href='([w]{3}\.[a-zA-Z]+\.+com)'></a>"

# "<h1>(.+?)</h1><a(.+?)></a>"
print(re.findall(pat, str))
# [('liuwei', 'www.baidu.com'), ('zhangbin', 'www.love.com')]