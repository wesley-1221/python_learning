# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月28日
"""

# class User:
#     def login(self):
#         print('欢迎来到登录页面')
#     def register(self):
#         print('欢迎来到注册页面')
#     def save(self):
#         print('欢迎来到存储页面')
# while 1:
#     choose = input('>>>').strip()
#     if choose == 'login':
#         obj = User()
#         obj.login()
#     elif choose == 'register':
#         obj = User()
#         obj.register()
#     elif choose == 'save':
#         obj = User()
#         obj.save()

# 反射
class User:
    def login(self):
        print('欢迎来到登录页面')
    def register(self):
        print('欢迎来到注册页面')
    def save(self):
        print('欢迎来到存储页面')
user = User()
while 1:
    choose = input('>>>').strip()
    if hasattr(user, choose):
        func = getattr(user, choose)
        func()
    else:
        print('输入错误。。。。')