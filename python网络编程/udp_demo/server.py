# -*- coding: utf-8 -*-
# @author: wesley
# @time: 2021/7/2:12:41
# @software: PyCharm

import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(("127.0.0.1", 9000))
# 需要知道谁发过来消息，client_addr
while True:
    msg, client_addr = sk.recvfrom(1024)
    print(msg.decode())
    inp = input('>>>').encode("utf-8")
    sk.sendto(inp, client_addr)

sk.close()

