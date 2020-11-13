# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月13日
"""

user_status = False                   #用户登陆了就改成True
def login(auth_type):                #把执行模块传进来
    def auth(func):
        def inner(*args, **kwargs):  #再定义一层函数
            if auth_type == "qq":
                _username = 'wesley'     #假设是数据库中的内容
                _password = '654321'
                global user_status
                if user_status == False:
                    username = input("user:")
                    password = input("password:")

                    if username == _username and password == _password:
                        print("welcome login...")
                        user_status = True
                    else:
                        print("wrong username or password!")

                if user_status == True:
                    return func(*args, **kwargs)           #只要这里通过了验证，就可以实验模块里面的功能
            else:
                print('only support qq')
        return inner
    return auth

def home():
    print("______首页_______")

@login('qq')
def america():
    print("______欧美专区______")

def japan():
    print("______日韩专区______")

@login('qq')
def henan(vip_level):
    #login()  # 执行前加上验证
    if vip_level > 3:
        print("解锁本专区所有高级玩法")
    else:
        print("----河南专区vip----")


home()
#america = login(america)
# america()
henan("5")


