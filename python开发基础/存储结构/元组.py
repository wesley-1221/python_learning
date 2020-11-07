# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月06日
"""

"""
不可变序列     字符串， 元组      看内存地址是不是发生了改变
可变序列       列表， 字典
"""

# #元组的创建
# tup = ('python', 'java', '99')
# print(tup, '\t', type(tup))
#
# tup1 = 'python', 'java', '99'             #没有小括号
# print(tup1, '\t', type(tup1))
#
# tup2 = ('python', )                        #元组只要单个元素的元组后面要加 逗号
# print(tup2, '\t', type(tup2))
#
# str = ('python')
# print(str, '\t', type(str))
#
#
# t = tuple(('python', 'java', '99'))
# print(t, '\t', type(t))
#
# #空元组
# tup5 = ()
# tup6 = tuple()


#引用不可变，整数不可变，列表里面可增删改查，但是列表中的引用不可变
tup = (10, 20, [1, 2])
# print(tup[0], type(tup[0]))
# print(tup[1], type(tup[1]))
# print(tup[2], type(tup[2]))

# tup[0] = 2              #TypeError: 'tuple' object does not support item assignment
# print(tup[0])
tup[2].append(3)
print(tup)                #(10, 20, [1, 2, 3])

#遍历元组
for i in tup:
    print(i, end = '\t')