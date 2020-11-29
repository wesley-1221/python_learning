# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月28日
"""

class Dog(object):
    def sound(self):
        print("汪汪汪.....")

class Cat(object):
    def sound(self):
        print("喵喵喵.....")


def make_sound(animal_obj):
    """统一调用接口"""
    animal_obj.sound() # 不管你传进来是什么动物，我都调用sound()方法

d = Dog()
c = Cat()

make_sound(d)
make_sound(c)