# -*- coding: utf-8 -*-
# @author: wesley
# @time: 2021/7/3:16:23
# @software: PyCharm

import socket
import json
import struct
import os

local_dir = r"F:\python_learn\python网络编程\文件下载进阶\local_dir"

sk = socket.socket()
sk.connect(('127.0.0.1', 9000))


def my_send(sk, dic, encoding='utf-8'):
    str_dic = json.dumps(dic)  # 先把字典转成str
    bdic = str_dic.encode(encoding)  # str转bytes
    dic_len = len(bdic)
    bytes_len = struct.pack('i', dic_len)  # 计算bytes长度
    sk.send(bytes_len)  # 发送长度
    sk.send(bdic)  # 发送字典


def my_recv(encoding='utf-8'):
    dic_len = sk.recv(4)  # 接收下载的文件信息
    dic_len = struct.unpack('i', dic_len)[0]
    dic = sk.recv(dic_len).decode(encoding)
    dic = json.loads(dic)
    return dic


def recv_file(filename, sk, dic, buffer=2048):
    def inner_recv(buffersize=buffer, recvsize=buffer):
        while dic['filesize'] > buffersize:
            content = sk.recv(recvsize)
            f.write(content)
            dic['filesize'] -= len(content)  # 收了多少减多少

    filepath = os.path.join(local_dir, filename)
    with open(filepath, 'wb') as f:
        inner_recv()
        inner_recv(0, dic['filesize'])


# 下载

filename = input('>>>')
dic = {'filename': filename, 'operate': 'download'}
my_send(sk, dic)
dic = my_recv()


if dic['isfile']:
    recv_file(filename, sk, dic)
else:
    print('文件不存在')



