# -*- coding: utf-8 -*-
# @author: wesley
# @time: 2021/7/3:11:38
# @software: PyCharm

import socket
import struct


sk = socket.socket()

sk.connect(('127.0.0.1', 9999))
msg = b'hello'
byte_len = struct.pack('i', len(msg))
sk.send(byte_len)
sk.send(msg)

msg = b'world!'
byte_len = struct.pack('i', len(msg))
sk.send(byte_len)
sk.send(msg)

sk.close()