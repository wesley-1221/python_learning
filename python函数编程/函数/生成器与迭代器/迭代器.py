# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月15日
"""

"""
可以作用于for循环的：
1. list, tuple, dict, set, str
2. generator, generator function
这些都叫    可迭代对象：iterable
"""
# 可以使用 isinstance() 判断是不是iterable对象

from collections import Iterable
print(isinstance([], Iterable))              # 用法     True

# 所有可以被next（）函数调用并且不断返回下一个值的对象叫 迭代器：Iterator
# 可用 isintance  判断
from collections import Iterator
print(isinstance([], Iterator))              # False
# 在前面加上 iter（）   就成为迭代器了
print(isinstance(iter([]), Iterator))        # True