# -*- coding: utf-8 -*-
# @author: wesley
# @time: 2021/7/3:15:40
# @software: PyCharm
'''
# 下载
    # 从哪个路径下载
    # 下载后放哪
        # 指定目录
        # 固定目录
'''
import socket
import json
import struct
import os

local_dir = r"F:\python_learn\python网络编程\文件上传\local_dir"

sk = socket.socket()
sk.connect(('127.0.0.1', 9000))

# 下载

filename = input('>>>')
dic = {'filename': filename, 'operate': 'download'}
str_dic = json.dumps(dic)              # 先把字典转成str
bdic = str_dic.encode('utf-8')         # str转bytes
dic_len = len(bdic)
bytes_len = struct.pack('i', dic_len)  # 计算bytes长度
sk.send(bytes_len)                     # 发送长度
sk.send(bdic)                          # 发送字典

dic_len = sk.recv(4)                   # 接收下载的文件信息
dic_len = struct.unpack('i', dic_len)[0]
dic = sk.recv(dic_len).decode('utf-8')
dic = json.loads(dic)

if dic['isfile']:
    filepath = os.path.join(local_dir, filename)
    with open(filepath, 'wb') as f:
        while dic['filesize'] > 2048:
            content = sk.recv(2048)
            f.write(content)
            dic['filesize'] -= len(content)         # 收了多少减多少
        else:
            while dic['filesize']:
                content = sk.recv(dic['filesize'])
                f.write(content)
                dic['filesize'] -= len(content)
else:
    print('文件不存在')




