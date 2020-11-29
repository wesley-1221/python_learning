# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月15日
"""

import json
import os
# # 将json类型的对象和json类型的字符串相互转化
# # {} 与 [] 嵌套的数据（python中建议从{}开始）
# #dumps
# dic = {
#     'a': 1,
#     'b': [1, 2, 3]
# }
# # 序列化将python的字典转化为字符串传递给其它语言或者保存
# json_str = json.dumps(dic)
# print(json_str, type(json_str))                        # {"a": 1, "b": [1, 2, 3]},<class 'str'>
#
# #dump
# if not os.path.exists('./json&pickle_test'):
#     os.mkdir('./json&pickle_test')
#     os.chdir('./json&pickle_test')
#     with open('jsonTest', 'w', encoding='utf-8') as fp:
#         json.dump(dic, fp)             # 先将dic对象转化为字符串，再写入文件

"""
loads和load 反序列化方法
反序列化成对象：json.loads(json_str)
从文件读流中反序列化成对象：json.load(read_file)
"""

# 反序列化
# json_str = "{'a': 1, 'b': [1, 2, 3, 4, 5]}"
# json类型的字符串不认单引号''
#loads
json_str = '''{"a": 1, "b": [1, 2, 3, 4, 5]}'''
new_dic = json.loads(json_str)
print(new_dic, type(new_dic))                 # {'a': 1, 'b': [1, 2, 3, 4, 5]} <class 'dict'>
# load
with open('./json&pickle_test/jsonTest', 'r', encoding='utf-8') as r:
    res = json.load(r)
    print(res, type(res))                     # {'a': 1, 'b': [1, 2, 3]} <class 'dict'>
