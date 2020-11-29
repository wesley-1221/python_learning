# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月13日
"""

account = {
    "is_authenticated":False,# 用户登录了就把这个改成True
    "username":"wesley", # 假装这是DB里存的用户信息
    "password":"654321" # 假装这是DB里存的用户信息
}


def login(func):

    def inner(*args,**kwargs):
        if account["is_authenticated"] is False:
            username = input("user:")
            password = input("pasword:")
            if username == account["username"] and password == account["password"]:
                print("welcome login....")
                account["is_authenticated"] = True
                func(*args, **kwargs) # 认证成功，执行功能函数
            else:
                print("wrong username or password!")
        else:
            print("用户已登录，验证通过...")
            func(*args, **kwargs)  # 认证成功，执行功能函数

    return inner


def home():
    print("---首页----")

@login
def america():
    #login()  # 执行前加上验证
    print("----欧美专区----")


def japan():
    print("----日韩专区----")

#@pay_money
@login #函数，装饰器，生成器，迭代器， 语法糖
def henan(vip_level):
    #login()  # 执行前加上验证
    if vip_level > 3:
        print("解锁本专区所有高级玩法")
    else:
        print("----河南专区vip----")

# america = login(america) # inner 的内存地址
# henan = login(henan)



home()
america() #inner()
henan(4) # inner(4)