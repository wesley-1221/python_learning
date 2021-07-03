# -*- coding: utf-8 -*-
# @author: wesley
# @time: 2021/7/3:11:38
# @software: PyCharm

import socket

sk = socket.socket()

sk.connect(('127.0.0.1', 9000))

sk.send('你好'.encode('utf-8'))

sk.send('不好'.encode('utf-8'))

sk.close()