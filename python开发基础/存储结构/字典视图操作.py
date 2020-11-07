# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月06日
"""

scores = {'wesley': '100', 'leo': '90'}
# print(scores.keys())               #获取全部键
# print(scores.values())             #获取全部值
# print(scores.items())              #获取全部键值对
# names = scores.keys()
# print(type(names), "\t", names)
# print(list(names))                   #将所有键转换成列表
#
# score = scores.values()
# print(list(score))
#
# item = scores.items()
# print(list(item))                    #元组组成的列表

#字典的遍历
for name in scores.keys():
    print(name)

#字典键不可以重复，重复会覆盖
print(scores)
scores['linda'] = 97
print(scores)
scores['linda'] = 98
print(scores)




