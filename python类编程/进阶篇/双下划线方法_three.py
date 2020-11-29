# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月29日
"""

# 重要
'''
str函数或者print函数调用时--->obj.__str__()
repr或者交互式解释器中调用时--->obj.__repr__()
如果__str__没有被定义,那么就会使用__repr__来代替输出
注意:这俩方法的返回值必须是字符串,否则抛出异常
'''
# class Student(object):
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         print("__触发了__repr__")
#         return "a"                  # 必须返回字符串
#
#     def __str__(self):
#         print("__触发了__str__")
#         return "a"                  # # 必须返回字符串
#
# s = Student("wesley", 18)
# print('from repr: ', repr(s))            # from repr:  a
# print('from str: ', str(s))              # from str:  a
# print(s)                                  # a

class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        print("__触发了__repr__")
        return 'Student(%s,%s)' %(self.name,self.age)

    def __str__(self):
        print("__触发了__str__")
        return '(%s,%s)' %(self.name,self.age)

s = Student("wesley", 18)
print('from repr: ', repr(s))            # from repr:  Student(wesley,18)
print('from str: ', str(s))              # from str:  (wesley,18)
print(s)                                   # (wesley,18)

