# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月29日
"""

# 设计模式

# 单例模式
"""
如何保证一个类只有一个实例并且这个实例易于被访问呢？定义一个全局变量可以确保对象随时都可以被访问，
但不能防止我们实例化多个对象。一个更好的解决办法是让类自身负责保存它的唯一实例。这个类可以保证没
有其他实例被创建，并且它可以提供一个访问该实例的方法。这就是单例模式的模式动机
"""


class Printer(object):
    __instance = None # 用来存唯一的一个实例
    __tasks = []
    def __init__(self,task):
        self.__tasks.append(task)
        print("added a new task in queue..",task)
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None: # 代表之前还没被实例化过
            obj = object.__new__(cls)
            cls.__instance = obj  # 把第一次实例化的对象 存下来，以后每次实例化都用这个第一次的对象
        return cls.__instance  # 下一次实例化时，就返回第一次实例化的对象
    def jobs(self):
        return self.__tasks
job = Printer("job1 word")
job2 = Printer("job2 png")
job3 = Printer("job3 excel")
print(id(job),id(job2),id(job3)) # 会发现这3个实例的内存id一样
print(job3.jobs())


