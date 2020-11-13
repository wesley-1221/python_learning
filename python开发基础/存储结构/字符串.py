# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月13日
"""

#字符串的创建
# var1 = 'hello world!'
# var2 = 'python'
#print(var1, '\t', var2)

#查
#print(var1[0])

#连接
# print(var1+var2)                         #hello world!python

#字符串运算符
# a = "Hello"
# b = "Python"
#
# print("a + b 输出结果：", a + b)
# print("a * 2 输出结果：", a * 2)
# print("a[1] 输出结果：", a[1])
# print("a[1:4] 输出结果：", a[1:4])
#
# if ("H" in a):
#     print("H 在变量 a 中")
# else:
#     print("H 不在变量 a 中")
#
# if ("M" not in a):
#     print("M 不在变量 a 中")
# else:
#     print("M 在变量 a 中")
#
# print(r'\n')
# print(R'\n')

#字符串格式化输出
# print ("我叫 %s 今年 %d 岁!" % ('小明', 10))

# f-string新的格式化字符串的语法,用了这种方式明显更简单了，不用再去判断使用 %s，还是 %d
name = "baby"
print(f'hello {name}')
print(f'{1+2}')
#3.6之后
w = {'name': 'Runoob', 'url': 'www.runoob.com'}
print(f'{w["name"]}: {w["url"]}')

# Python 3.8 的版本中可以使用 = 符号来拼接运算表达式与结果
# print(f'{x+1=}')               #3.8之后才可以用           'x+1=2'

#字符串内置函数







