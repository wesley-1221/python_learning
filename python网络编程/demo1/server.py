# -*- coding: utf-8 -*-
# @author: wesley
# @time: 2021/6/30:15:10
# @software: PyCharm

import socket

sk = socket.socket()              # 买手机
sk.bind(('127.0.0.1', 9000))    # 绑定卡号
sk.listen()                     # 开机

conn, addr = sk.accept()         # 等着接电话
conn.send(b'hello')              # 发信息
msg = conn.recv(1024)            # 收信息
print(msg)

conn.close()            # 挂电话
sk.close()              # 关机 （占用操作系统资源）

