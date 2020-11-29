# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月28日
"""

# 可以通过字符串的形式来操作对象的属性

"""
这里我们可以看到有什么属性， 程序运行的时候不知道有什么属性，需要判断，如果没有，
会报错，为了避免报错，判断有没有该属性
"""

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print('walking........')

def talk(self):                                  # 给类绑定方法
    print(self.name, "is speaking")

p = Person("wesley", 18)

# if p.name2:                     # 这里直接调用了，没有就报错
#     print("l....")
# hasattr
if hasattr(p, 'name2'):          # 判断p对象中有没有 name2 这个属性
    print('l.........')

if hasattr(p, 'name'):           # 判断p对象中有没有 name2 这个属性
    print('有')                   # 有

"""
# 反射, 映射， 自省
# getattr()     # 获取
# hasattr()     # 判断
# setattr()     # 赋值
# delattr()     # 删除
"""

# getattr
name = getattr(p, 'name')       # 用户不知道源码，他们只是键盘输入，不知道有什么属性
print(name)

# getattr hasattr
# 人机交互                       # 非常有用
# user_command = input(">>:".strip())
# if hasattr(p, user_command):
#     func = getattr(p, user_command)     # user_command 一个字符串,赋值给func
#     func()

# setattr
# static属性
setattr(p, 'sex', 'female')            # 设置性别
print(p.sex)                             # female
# 动态方法
# setattr(p, "speak", talk)              # 给实例绑定
# p.speak(p)                             # 需要手动传传参
# 在Person类中绑定talk这个方法,给speak2
setattr(Person, 'speak2', talk)         # 给类绑定
p.speak2()                               # 自动传

# delattr() == del p.age
delattr(p, "age")
p.age                                    # AttributeError: 'Person' object has no attribute 'age'
