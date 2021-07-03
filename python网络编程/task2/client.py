# -*- coding: utf-8 -*-
# @author: wesley
# @time: 2021/7/2:15:45
# @software: PyCharm

import json
import socket

usr = input("username:")
pwd = input("password:")
dic = {'usr': usr, 'pwd': pwd}

str_dic = json.dumps(dic)
sk = socket.socket()
sk.connect(('127.0.0.1', 9000))

sk.send(str_dic.encode('utf-8'))

ret = sk.recv(1024).decode('utf-8')
dic_ret = json.loads(ret)
if dic_ret['result']:
    print("登录成功")
