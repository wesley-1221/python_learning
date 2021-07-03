# -*- coding: utf-8 -*-
# @author: wesley
# @time: 2021/7/2:15:27
# @software: PyCharm
import json
import socket

sk = socket.socket()
sk.connect(("127.0.0.1", 9999))

# 中文要编码，utf-8/gbk都行。因为只要转成二进制就行
while True:
    inp = input(">>>")
    uid = "12345"
    dic = {"msg": inp, "uid": uid}
    str_dic = json.dumps(dic)
    sk.send(str_dic.encode('utf-8'))
    # sk.send("|".join([name, inp]).encode('utf-8'))
    if inp.upper() == "Q":
        break
    msg = sk.recv(1024).decode("utf-8")
    if msg.upper() == "Q":
        break
    print(msg)

sk.close()
