# -*- coding: utf-8 -*-
# @author: wesley
# @time: 2021/7/3:12:31
# @software: PyCharm

import socket
import time

sk = socket.socket()

sk.connect(('127.0.0.1', 9000))

for i in range(20):
    sk.send(b"leo")
    msg = sk.recv(1024)
    print(msg)
    time.sleep(0.2)