# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月28日
"""

class Dog:
    def __init__(self,name,age,breed,master):
        self.name = name
        self.age = age
        self.breed = breed
        self.master = master # master传进来的应该是个对象
        self.sayhi()  # 调用自己的方法在实例化的时候 ，实例化之后自动调用sayhi()
    def sayhi(self):
        print("Hi, I'm %s, a %s dog, my master is %s" %(self.name,self.breed,self.master.name))
class Person:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def walk_dog(self,dog_obj):
        """遛狗"""
        print("主人[%s]带狗[%s]去溜溜。。。" % (self.name,dog_obj.name ))
p = Person("杨某",18,"Male")             # 作为一个对象传入Dog类中
d = Dog("李某", 5, "二哈", p)
p.walk_dog(d)