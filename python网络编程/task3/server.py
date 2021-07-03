# -*- coding: utf-8 -*-
# @author: wesley
# @time: 2021/7/2:16:46
# @software: PyCharm

# 上传文件
# (不是一个完美的文件传输，如果两台电脑通信，需要经过交换机
# 那么文件的就会变小。)

import socket
import json

sk = socket.socket()
sk.bind(("127.0.0.1", 9000))
sk.listen()

conn, _ = sk.accept()
str_dic = conn.recv(1024)
dic = json.loads(str_dic)

content = conn.recv(dic["filesize"])
with open(dic["filename"], mode="wb") as f:
    f.write(content)


conn.close()
sk.close()

