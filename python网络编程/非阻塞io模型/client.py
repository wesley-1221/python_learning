# -*- coding: utf-8 -*-
# @author: wesley
# @time: 2021/7/3:12:09
# @software: PyCharm

import socket
import time

sk = socket.socket()

sk.connect(('127.0.0.1', 9000))

while True:
    sk.send(b"wesley")
    msg = sk.recv(1024)
    print(msg)
    time.sleep(0.5)


# sk.close()



