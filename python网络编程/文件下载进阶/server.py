# -*- coding: utf-8 -*-
# @author: wesley
# @time: 2021/7/3:16:23
# @software: PyCharm

import socketserver
import struct
import json
import os

server_dir = r"F:\python_learn\python网络编程\文件下载进阶\server_dir"


class Myserver(socketserver.BaseRequestHandler):

    def my_recv(self, encoding='utf-8'):
        dic_len = self.request.recv(4)
        dic_len = struct.unpack('i', dic_len)[0]
        dic = self.request.recv(dic_len).decode(encoding)
        dic = json.loads(dic)
        return dic

    def my_send(self, dic, encoding='utf-8'):
        str_dic = json.dumps(dic)  # 先把字典转成str
        bdic = str_dic.encode(encoding)  # str转bytes
        dic_len = len(bdic)
        bytes_len = struct.pack('i', dic_len)  # 计算bytes长度
        self.request.send(bytes_len)  # 发送长度
        self.request.send(bdic)  # 发送字典

    def send_file(self, dic, filepath):
        with open(filepath, 'rb') as f:
            while dic['filesize'] > 2048:
                content = f.read(2048)
                self.request.send(content)
                dic['filesize'] -= len(content)
            else:
                content = f.read()
                self.request.send(content)

    def download(self, dic):
        filename = dic['filename']
        filepath = os.path.join(server_dir, filename)
        dic = {}
        if os.path.isfile(filepath):
            dic['filesize'] = os.path.getsize(filepath)
            dic['isfile'] = True
            self.my_send(dic)
            self.send_file(dic, filepath)
        else:
            dic['isfile'] = False
            self.my_send(dic)

    # 这段代码,每个客户端进来都要从头执行
    def handle(self):         # 一旦有客户端连接，自动触发
        dic = self.my_recv()
        if dic['operate'] == 'download':
            self.download(dic)






server = socketserver.ThreadingTCPServer(('127.0.0.1', 9000), Myserver)
server.serve_forever()            # 一直启动server
