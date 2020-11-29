# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月28日
"""

# 类方法通过@classmethod装饰器实现，类方法和普通方法的区别是， 类方法只能访问类变量，不能访问实例变量

# class Dog(object):
#     name = "毛某"                  # dog 毛某 is eating...
#     def __init__(self, name):
#         self.name = name
#
#     """
#     有什么用？ （没有什么用）
#     """
#     @classmethod                   # 不可以访问实例变量，只能访问类变量
#     def eat(cls):
#         # print(cls)              # <class '__main__.Dog'>代表类本身，不是dog对象
#         print("dog %s is eating..."%cls.name)              # AttributeError: type object 'Dog' has no attribute 'name'
#
#     def play(self):
#         # print(self)              # <__main__.Dog object at 0x000001CCC2C22B88> 实例本身
#         print("dog %s is playing..."%self.name)             # dog 李某 is eating...
#
# d = Dog('李某')
# d.eat()
# d.play()


# @classmethod  用处
class Student(object):
    __stu_num = 0
    def __init__(self, name):
        self.name = name
        # self.stu_num += 1                # 这里不是类变量加一， 而是生成实例变量 对实例进行赋值
        # Student.stu_num += 1               # 也可以在外面加一， 但是不允许在外面加，所有用到类方法
        # print("生成一个学生", name, Student.stu_num)
        # elf.add_stu()
        self.add_stu(self)                 # 实例本身s1
    @classmethod
    def add_stu(cls, obj):                      # 防止用户作弊， 但是可以直接调用这个方法也加一
        if obj.name:                             # 生成实例才加一
            cls.__stu_num += 1
            print("生成一个新学生", cls.__stu_num)


s1 = Student('李某')
s2 = Student('毛某')




