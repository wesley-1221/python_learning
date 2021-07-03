# -*- coding: utf-8 -*-
# @author: wesley
# @time: 2021/7/3:13:30
# @software: PyCharm

import os
import hashlib
import socket


def get_md5(secret_key, randseq):
    md5 = hashlib.md5(secret_key)
    md5.update(randseq)
    res = md5.hexdigest()
    return res


def chat(conn):
    while True:
        msg = conn.recv(1024).decode('utf-8')
        print(msg)
        conn.send(msg.upper().encode('utf-8'))


sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen()

secret_key = b"wesley"                 # 密钥 字节

conn, addr = sk.accept()

# 发送随机字符串
randseq = os.urandom(32)             # 随机字符串 已经是二进制的了
conn.send(randseq)

# md5算法
md5_code = get_md5(secret_key, randseq)

# 接收
ret = conn.recv(32).decode('utf-8')
# 判断
if md5_code == ret:
    print("是合法客户端")
    chat(conn)
else:
    print("不是合法客户端")

conn.close()
sk.close()
