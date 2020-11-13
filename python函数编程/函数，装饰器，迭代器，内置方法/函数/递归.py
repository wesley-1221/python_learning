# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月13日
"""

# 内部调用自身
# def calc(n):
#     print(n)
#     if int(n/2) == 0:
#         return n
#     return calc(int(n/2))
# calc(10)

def calc(n):
    v = int(n/2)
    print(v)
    if v > 0:
        calc(v)
    print(n)                  # 全部递归之后才输出

calc(10)