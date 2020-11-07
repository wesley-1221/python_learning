# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月06日
"""
"""
#字典的创建
scores = {'wesley':'100','leo':'90'}
print(scores,type(scores))

age = dict(wesley = '20',leo = '21')
print(age, type(age))

#空字典
d = {}
print(d)
"""

#查
# scores = {'wesley': '100', 'leo': '90'}
# print(scores['wesley'])
# #print(scores['linda'])              #KeyError: 'linda'
#
# print(scores.get('wesley'))
# print(scores.get('linda'))          #不会报错，None
# print(scores.get('叶宝宝', 99))      #在字典中查找叶宝宝，没有查到就输出99，99是默认值，而不是赋值
# print(scores)
"""
#in   not in (判断)
scores = {'wesley': '100', 'leo': '90'}
print('wesley' in scores)
print('wesley' not in scores)

#del删除
del scores['leo']             #删除指定键值对 {'wesley': '100'}
print(scores)
scores.clear()                 #{}    清空
print(scores)
"""

#增
scores = {'wesley': '100', 'leo': '90'}

scores['linda'] = 95                #{'wesley': '100', 'leo': '90', 'linda': 95}
print(scores)

#改
scores = {'wesley': '100', 'leo': '90'}
scores['leo'] = 98                  #{'wesley': '100', 'leo': 98}
print(scores)










