# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月04日
"""
"""
整数
十进制
二进制 0b开头
八进制 0o开头
十六进制 0x开头
"""
#整型  int  整数，负数，0
#浮点型  float
"""
浮点数存储不精确，计算是可能出错
需要导入模块
"""
x = 1.1
y = 2.2
print(x+y)      #3.3000000000000003 可能出错
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))
#布尔型  bool   True（1），False（0）
s = True
print(type(s))
print(s+1)       #bool型可当作整型计算
#字符串型  “字符”

