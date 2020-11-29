# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月28日
"""



class Animal:
    a_type = "哺乳动物"

    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        print("----父类的构造方法")

    def eat(self):
        print("%s is eating...." % self.name)


class Person(Animal):
    a_type = "哺乳高等动物"

    def __init__(self,name,age,sex,hobbie):
        #Animal.__init__(self,name,age,sex)
        #super(Person,self).__init__(name,age,sex) # 效果同上，py3          #Person当前类，self实例本身
        super().__init__(name, age, sex)  # 跟上面这行super语法的效果一样，一般用这种写法的多
        self.hobbie = hobbie
        print("----子类的构造方法")

    def talk(self):
        print("person %s is talking..." % self.name)

    def eat(self):
        #Animal.eat(self)
        super().eat() # 执行父类的方法
        print("人在优雅的吃。。。。")


class Dog(Animal):
    def chase_rabbit(self):
        print("狗在追究兔子。。。。")


p = Person("李某",22,"M","篮球")
p.eat()
p.talk()

print(p.name,p.sex,p.hobbie)

# d = Dog("Mjj",3,"Female")
# d.eat()
# print(d.a_type)
# d.chase_rabbit()
