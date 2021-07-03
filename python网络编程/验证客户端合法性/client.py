# -*- coding: utf-8 -*-
# @author: wesley
# @time: 2021/7/3:13:30
# @software: PyCharm

import socket
import hashlib
import time


def get_md5(secret_key, randseq):
    md5 = hashlib.md5(secret_key)
    md5.update(randseq)
    res = md5.hexdigest()
    return res


def char(sk):
    while True:
        sk.send(b'wesley')
        msg = sk.recv(1024).decode('utf-8')
        print(msg)
        time.sleep(0.3)


sk = socket.socket()
sk.connect(('127.0.0.1', 9000))

secret_key = b"wesley"        # 密钥两边一致
randseq = sk.recv(32)         # 接收随机字符串
# 加密
md5_code = get_md5(secret_key, randseq)
# 发送
sk.send(md5_code.encode('utf-8'))

char(sk)

sk.close()


