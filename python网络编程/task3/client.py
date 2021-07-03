# -*- coding: utf-8 -*-
# @author: wesley
# @time: 2021/7/2:16:46
# @software: PyCharm


import socket
import os
import json

sk = socket.socket()
sk.connect(('127.0.0.1', 9000))

file_path = input("绝对路径>>>")
if os.path.abspath(file_path):
    filename = os.path.basename(file_path)
    filesize = os.path.getsize(file_path)          # 文件大小，server接收的时候要写的大小
    dic = {"filename": filename, "filesize": filesize}
    str_dic = json.dumps(dic)
    sk.send(str_dic.encode('utf-8'))
    with open(file_path, mode='rb') as f:          # rb 已经是二进制了
        content = f.read()
        sk.send(content)


sk.close()

