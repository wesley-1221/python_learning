# -*- coding: utf-8 -*-
# @author: wesley
# @time: 2021/6/30:15:10
# @software: PyCharm

import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 9000))

msg = sk.recv(1024)
print(msg)
sk.send(b'byebye')

sk.close()

