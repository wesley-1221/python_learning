# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月15日
"""

import hashlib
#任意长度的输入》》》hash》》》固定长度的输出


# # md5加密算法
# m = hashlib.md5()
# print(m.digest())
# m.update(b"hello")
# print(m.digest())
# m.update(b"it`s me")
# print(m.digest())                    # 二进制格式hash b'TO^\xbb\x93D\xf7\x98\xb8]\xa5\xd0\xdf;(\x11'
# print(len(m.hexdigest()))            # 16进制格式

# md5（唯一性）
hash = hashlib.md5()
hash.update(b'admin')
print(hash.hexdigest())                           #21232f297a57a5a743894a0e4a801fc3

# sha1
hash = hashlib.sha1()
#python3中字符对象是unicode对象，不能直接加密
#hash.update('admin')
hash.update('admin'.encode('utf-8'))            # d033e22ae348aeb5660fc2140aec35850c4da997
print(hash.hexdigest())

# sha256
hash = hashlib.sha256()
hash.update('admin'.encode('utf-8'))            # 8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918
print(hash.hexdigest())

# sha384
hash = hashlib.sha384()
hash.update('admin'.encode('utf-8'))            # 9ca694a90285c034432c9550421b7b9dbd5c0f4b6673f05f6dbce58052ba20e4248041956ee8c9a2ec9f10290cdc0782
print(hash.hexdigest())

# sha512
hash = hashlib.sha512()
hash.update('admin'.encode('utf-8'))            # c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec
print(hash.hexdigest())






