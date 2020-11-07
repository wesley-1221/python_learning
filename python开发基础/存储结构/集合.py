# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月06日
"""
"""
#集合的创建    特点：无序，不会有重复元素
s = {1, 2, 3, 3, 4}
#print(s)                      #{1, 2, 3, 4}
# s1 = set({1, 2, 3, 3, 4})
# print(s1)

#无序
s2 = set("python")            #{'n', 'h', 'o', 'y', 't', 'p'}
print(s2)
"""
#
# #判断操作（in   not in）
# s = {1, 2, 3, 3, 4}
# print(10 in s)
#
# #增
# #增加一个元素
# s.add(80)              #{1, 2, 3, 4, 80}
# print(s)
# #增加多个元素
# s.update({100, 200})
# print(s)
#
# s.update([300, 200])
# print(s)

# #删
# s = {1, 2, 3, 4, 100, 200, 300, 80}
# s.remove(80)             #没有会报错
# print(s)
# s.discard(500)           #没有不会报错
# print(s)
# s.pop()                  #删除任意（随机）一个元素(不可以添加参数)
# print(s)
# s.clear()                #清空
# print(s)

#特点
# s = {1, 2}
# s1 = {2, 1}
# print(s == s1)                  #True

#判断子集
s1 = {}



