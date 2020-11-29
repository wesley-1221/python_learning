# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月29日
"""

class Person(object):
    def __init__(self,name):
        self.name = name
        print("--init ....")
    def __new__(cls, *args, **kwargs):
        # 决定是否执行__init__, 进行一些初始化工作
        """
        cls  : 代表Person这个类本身
        :param args:
        :param kwargs:
        :return:
        """
        print("--in new: ",cls,*args,**kwargs)
        return object.__new__(cls)  # 调用父类的__new__方法，必须这么干 ，要不然__init__方法就不会执行了
p = Person("wesley")
print(p.name)
print(Person)