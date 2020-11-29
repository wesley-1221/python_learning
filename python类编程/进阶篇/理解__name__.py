# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月28日
"""
"""
__name__ 在当前模块主动执行的情况下（不是被导入）， 等于__main__
         在被其它模块导入的情况下，输出模块名
"""


print(__name__)           # __main__ 就代表模块本身

if __name__ == "__main__":   # 只会在被其它模块导入的时候才发挥作用
    # 在这里用__name__    被主动执行，就执行下面的函数
    # 不是主动执行， 就不执行下面的语句
    print("-----------")

"""
__main__
-----------
"""

import sys

# for k, v in sys.modules.items():
#     print(k, v)          # __main__ <module '__main__' from 'G:/python_learn/python类编程/进阶篇/理解__name__.py'>

# print(sys.modules["__main__"])
print(sys.modules[__name__])






