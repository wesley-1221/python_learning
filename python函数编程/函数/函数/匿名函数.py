# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月13日
"""

def calc(x, y):
    return x**y

print(calc(2, 3))
# 匿名函数，结果相同
calc = lambda x,y:x**y
print(calc(2, 3))

#匿名函数结合其它函数一起使用
res = map(lambda x:x**2, [1, 2, 3])
print(res)
for item in res:
    print(item)



