# -*- coding: utf-8 -*-
# @author: wesley
# @time: 2021/7/2:14:55
# @software: PyCharm

import json
import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 9999))
sk.listen()           # 监听  n 允许多少人等
color_dic = {
    "12345": {"color": "\033[34m", "name": "wesley"},
    "123456": {"color": "\033[33m", "name": "叶宝宝"}
}
# print("****")
while True:
    conn, addr = sk.accept()           # 阻塞（类似于input 输入才执行。这个是有人连接才执行后面代码）
    # print("有人来连接我了")
    while True:
        # 收信息
        msg = conn.recv(1024).decode('utf-8')
        dic_data = json.loads(msg)
        # name, msg = msg.split("|")
        if msg.upper() == "Q":
            break
        # print("%s: %s" % (name, msg))
        uid = dic_data["uid"]
        print("%s%s: %s\033[0m" % (color_dic[uid]["color"], color_dic[uid]["name"], dic_data["msg"]))
        # 发信息
        inp = input(">>>")
        conn.send(inp.encode("utf-8"))
        if inp.upper() == "Q":
            break

    conn.close()
# sk.close()