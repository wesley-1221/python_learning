# -*- coding: utf-8 -*-
# @author: wesley
# @time: 2021/7/3:14:29
# @software: PyCharm

import socketserver


class Myserver(socketserver.BaseRequestHandler):
    # 这段代码,每个客户端进来都要从头执行
    def handle(self):         # 一旦有客户端连接，自动触发
        # print(self.request)   # self.request == conn
        while True:
            msg = self.request.recv(1024).decode('utf-8')
            print(msg)
            self.request.send(msg.upper().encode('utf-8'))



server = socketserver.ThreadingTCPServer(('127.0.0.1', 9000), Myserver)
server.serve_forever()            # 一直启动server


