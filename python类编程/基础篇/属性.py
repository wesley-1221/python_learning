# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月28日
"""

# 类的各种属性
# class People(object):
#     # nationality 存中国这里的国籍相同，实例变量存储浪费内存，应该使用类变量
#     def __init__(self, name, sex, age, nationality):
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.nationality = nationality
#
# p = People("李某", "男", 18, "中国")
# p2 = People("毛某", "男", 19, "中国")
# print(p.nationality)

# class People(object):
#     nationality = "中国"             #共有属性用类变量
#     def __init__(self, name, sex, age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
# p = People("李某", "男", 18)
# p2 = People("毛某", "男", 19)
# print(People.nationality)
# print(p.nationality)

class People(object):
    nationality = "中国"
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age

p = People("李某", "男", 18)
p2 = People("毛某", "男", 19)
# 如果一个人需要改变国籍
# p2
p2.nationality = "美国"                    # 只是p2的国籍改变了，其他人不变
print(p2.nationality)
print(People.nationality)