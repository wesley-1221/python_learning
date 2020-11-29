# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月15日
"""
# dumps, loads
import pickle
import os

# dic = {
#     'a': 1,
#     'b': [1, 2, 3]
# }
#转化成只有python才懂的数据
# p_str = pickle.dumps(dic)
# print(p_str, type(p_str))         # b'\x80\x03}q\x00(X\x01\x00\x00\x00aq\x01K\x01X\x01\x00\x00\x00bq\x02]q\x03(K\x01K\x02K\x03eu.' <class 'bytes'>
#
# data = pickle.loads(p_str)
# print(data, type(data))           # {'a': 1, 'b': [1, 2, 3]} <class 'dict'>

# dump, load

dic = {
    'a': 1,
    'b': [1, 2, 3]
}
with open('./json&pickle_test/pickle_test', 'wb') as fp:
    pickle.dump(dic, fp)

with open('./json&pickle_test/pickle_test', 'rb') as r:            # 注意mode = rb
    res = pickle.load(r)
    print(res, type(res))
