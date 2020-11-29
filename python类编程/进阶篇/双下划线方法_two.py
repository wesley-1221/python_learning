# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月29日
"""

class Dict(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 获取
    def __getitem__(self, item):
        print(item)                     # name
        print("__触发getitem__")
        print(self.__dict__)            # {'name': 'wesley', 'age': 18}
        print(self.__dict__[item])      # wesley
    # 改，增
    def __setitem__(self, key, value):
        print("__触发__setitem")
        print(key, "\t", value)        # name 	 leo
        print(self.__dict__)            # 还没改{'name': 'wesley', 'age': 18}
        self.__dict__[key] = value      # 改变
        print(self.__dict__)            # {'name': 'leo', 'age': 18}

    def __delitem__(self, key):
        print("__触发__delitem__")
        self.__dict__.pop(key)

    def __delattr__(self, item):
        print(item)
        print("触发__delitem__")
        self.__dict__.pop(item)

d = Dict("wesley", 18)
# print(d.name)
# # 字典方式获取
# # print(d["name"])                   # TypeError: 'Dict' object is not subscriptable
# # 获取
# d["name"]                           # __触发getitem__
# # 改
# d["name"] = "leo"                  # TypeError: 'Dict' object does not support item assignment
# # 增
# d["sex"] = "Male"                  # {'name': 'leo', 'age': 18, 'sex': 'Male'}
# # 删除
# # del d["sex"]                       # AttributeError: __delitem__
# print("+++++++++++++++++++++++++++++++++++++++++++++")
# del d["sex"]
# d["name"]                           # {'name': 'leo', 'age': 18}

print(d.__dict__)
del d.age                            # 触发__delattr
print(d.__dict__)











