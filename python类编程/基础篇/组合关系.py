# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月28日
"""


# 由一堆组件构成一个完整的实体， 组件本身独立，但又不能自己运行，必须跟宿主组合在一起，运行


class Dog:  # 定义一个狗类
    role = 'dog'  # 狗的角色属性都是狗

    def __init__(self, name, breed, attack_val):
        self.name = name
        self.breed = breed  # 每一只狗都有自己的品种;
        self.attack_val = attack_val  # 每一只狗都有自己的攻击力;
        self.life_val = 100  # 每一只狗都有自己的生命值;

    def bite(self, person):
        # 狗可以咬人，这里传递进来的person也是一个对象。
        person.life_val -= self.attack_val # 狗咬人，那么人的生命值就会根据狗的攻击力而下降

        print("狗[%s]咬了人[%s],人掉血[%s],还剩血量[%s]..." % (self.name,person.name,self.attack_val,person.life_val))


class Weapon:

    def dog_stick(self, obj):
        """打狗棒"""
        self.name = "打狗棒"
        self.attack_val = 40
        obj.life_val -= self.attack_val
        self.print_log(obj)

    def knife(self, obj):
        """屠龙刀"""
        self.name = "屠龙刀"
        self.attack_val = 80
        obj.life_val -= self.attack_val
        self.print_log(obj)

    def gun(self, obj):
        """AK47"""
        self.name = "AK47"
        self.attack_val = 100
        obj.life_val -= self.attack_val
        self.print_log(obj)

    def print_log(self, obj):
        print("[%s]被[%s]攻击了，掉血[%s],还剩血量[%s]..." % (obj.name, self.name, self.attack_val, obj.life_val))


class Person:  # 定义一个人类
    role = 'person'  # 人的角色属性都是人

    def __init__(self, name, sex, attack_val):
        self.name = name
        #self.attack_val = attack_val
        self.life_val = 100
        self.sex = sex
        self.weapon = Weapon() # 直接实例化

    # def attack(self,dog):
    #     # 人可以攻击狗，这里传递进来的dog也是一个对象。
    #     # 人攻击狗，那么狗的生命值就会根据人的攻击力而下降
    #     dog.life_val -= self.attack_val
    #     print("人[%s]打了狗[%s],狗掉血[%s],还剩血量[%s]..." % (self.name,dog.name,self.attack_val,dog.life_val))
    #



d = Dog("李某","二哈",30)
p = Person("毛某","M",50)

d.bite(p)
p.weapon.gun(d)
p.weapon.knife(d)

