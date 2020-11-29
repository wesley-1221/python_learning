# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月15日
"""

import random

print(random.randrange(1, 10))           # 返回1-9任意一个随机数
print(random.randint(1, 10))             # 返回1-10任意一个随机数
print(random.randrange(0, 100, 2))       # 返回偶数
print(random.random())                   # 随机浮点数
print(random.choice('asfghjkl'))        # 随机一个给定的字母
print(random.sample('asdflds', 3))      # 随机三个       ['d', 'a', 'd']构成列表

# 生成随机字符串
import string
"""
其中ascii_letters是生成所有字母，从a-z和A-Z
digits是生成所有数字0-9
"""
str1 = ''.join(random.sample(string.ascii_lowercase + string.digits, 6))           # 小写
str2 = ''.join(random.sample(string.ascii_letters + string.digits, 6))             # 大小写
str3 = ''.join(random.sample(string.ascii_uppercase + string.digits, 6))           # 大写
print(str1)
print(str2)
print(str3)

# 洗牌
a = [i for i in range(11)]
print(a)
random.shuffle(a)
print(a)
"""
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[7, 4, 10, 6, 2, 1, 9, 5, 3, 0, 8]
"""




