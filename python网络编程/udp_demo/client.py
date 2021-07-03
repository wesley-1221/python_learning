# -*- coding: utf-8 -*-
# @author: wesley
# @time: 2021/7/2:12:42
# @software: PyCharm

import socket

sk = socket.socket(type=socket.SOCK_DGRAM)

while True:
    inp = input('>>>').encode("utf-8")
    sk.sendto(inp, ("127.0.0.1", 9000))

    msg = sk.recv(1024).decode()
    print(msg)

sk.close()
