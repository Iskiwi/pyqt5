# -*- coding: utf-8 -*-
# @Time    : 2021/10/6 12:23
# @Author  : B612
# @File    : 02-search.py

import re

string = "Cats are smarter than dogs"
res1 = re.match("dogs", string)
res2 = re.search("dogs", string)
print(res1, res2.group())  # None dogs