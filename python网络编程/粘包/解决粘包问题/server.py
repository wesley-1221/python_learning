# -*- coding: utf-8 -*-
# @author: wesley
# @time: 2021/7/3:11:38
# @software: PyCharm

import socket
import time
import struct

sk = socket.socket()
sk.bind(('127.0.0.1', 9999))
sk.listen()

conn, _ = sk.accept()
time.sleep(0.1)
byte_len = conn.recv(4)
msg_len = struct.unpack('i', byte_len)[0]     # unpack结果  是一个元组 取第一个
msg_1 = conn.recv(msg_len)

print(msg_1)
byte_len = conn.recv(4)
msg_len = struct.unpack('i', byte_len)[0]
msg_2 = conn.recv(msg_len)
print(msg_2)

conn.close()
sk.close()