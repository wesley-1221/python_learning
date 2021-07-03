# -*- coding: utf-8 -*-
# @author: wesley
# @time: 2021/7/3:12:09
# @software: PyCharm

# 异步io模型
import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.setblocking(False)
sk.listen()

conn_list = []
del_list = []
while True:
    try:
        conn, addr = sk.accept()
        print(conn)
        conn_list.append(conn)
    except BlockingIOError:
        for c in conn_list:
            try:
                msg = c.recv(1024).decode('utf-8')
                if not msg:                         # 当客户端退出时，msg为空，将它加入列表，后面删除。
                    del_list.append(c)
                    continue
                print([msg])
                c.send(msg.upper().encode('utf-8'))
            except BlockingIOError:
                pass
        for c in del_list:
            conn_list.remove(c)
        del_list.clear()              # 清空del_list

# 并发，但是做了很多无用功。
# 框架   io异步+io多路复用





