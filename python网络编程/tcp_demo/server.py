# -*- coding: utf-8 -*-
# @author: wesley
# @time: 2021/7/2:11:48
# @software: PyCharm

import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 9999))
sk.listen()           # 监听  n 允许多少人等
# print("****")
while True:
    conn, addr = sk.accept()           # 阻塞（类似于input 输入才执行。这个是有人连接才执行后面代码）
    # print("有人来连接我了")
    while True:
        # 收信息
        msg = conn.recv(1024).decode('utf-8')
        if msg.upper() == "Q":
            break
        print(msg)
        # 发信息
        inp = input(">>>")
        conn.send(inp.encode("utf-8"))
        if inp.upper() == "Q":
            break

    conn.close()
# sk.close()
