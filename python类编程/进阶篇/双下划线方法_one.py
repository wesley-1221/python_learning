# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月29日
"""

# __len__
# __hash__
# __eq__

class Student(object):

    def __init__(self, name):
        self.name = name

    def __len__(self):
        print("____len____")
        return 1                    # 需要返回一个整数

    def __hash__(self):
        print("____hash____")
        return 2

    def __eq__(self, other):
        print(other.name)
        print("call eq method.")
        if self.name == other.name and self.name == other.name:
            return True
        else:
            print("不相等 ")
            return False

s = Student("wesley")
s1 = Student("linda")
len(s)                          # 触发__len__
# print(hash(s))                # -922337184451311246 没有重写__hash__
hash(s)                         # 触发__hash__
s == s1                         # 触发__eq__
print("__________________________________________________")






