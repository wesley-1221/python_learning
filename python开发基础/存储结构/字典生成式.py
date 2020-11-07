# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月06日
"""

#内置函数zip()

# names = ['wesley', 'leo', 'linda']
# scores = ['100', '99', '98']
# dic ={names:scores for names, scores in zip(names, scores)}
# d ={names.upper():scores for names, scores in zip(names, scores)}            #names.upper()  names变大写
# print(dic)
# print(d)

#当两个列表元素个数不同时，会以少的为准
names = ['wesley', 'leo', 'linda', '叶宝宝']
scores = ['100', '99', '98']
dic ={names:scores for names, scores in zip(names, scores)}
d ={names.upper():scores for names, scores in zip(names, scores)}            #names.upper()  names变大写

print(d)