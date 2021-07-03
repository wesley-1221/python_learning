# -*- coding: utf-8 -*-
# @author: wesley
# @time: 2021/7/3:11:38
# @software: PyCharm

# 出现粘包现象，（原因tcp协议，os）

import socket
import time

sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()

conn, _ = sk.accept()
time.sleep(1)
x = conn.recv(1024).decode('utf-8')
y = conn.recv(1024).decode('utf-8')

print(x)
print(y)

conn.close()
sk.close()
