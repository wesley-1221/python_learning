# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月04日
"""

num_a = int(input('请输入一个数字:\n'))
num_b = int(input('请输入一个数字：\n'))

print('使用条件表达式进行比较两个数')
#int型不可以于str型进行拼接
#True输出前面，False输出后面
print(str(num_a)+'大于'+str(num_b)  if num_a>num_b else  str(num_a)+'小于' +str(num_b))