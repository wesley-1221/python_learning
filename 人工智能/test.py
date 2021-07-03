# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年12月04日
"""

# # s = {'a':100,'b':90}
# # print([k for k, v in s.items() if v==100])
#
# dic = {'apple': [('red', 'big'), ('red', 'cirle')]}
# # print([k for k,v in dic.items() if [('red', 'big'), ('red', 'cirle')] in dic.values()])
#
# # s = [('red', 'big'), ('red', 'cirle')]
# # b = ('red', 'big')
# # print(b in s)
#
# # for k,v in dic.items():
# for k,v in dic.items():
#     if ('red', 'big') in v:
#         print(k)

# import json
# json_dic = {'c': [{'a', 'b'}, {'bbb', 'aaa'}], 'cc': [{'aa', 'bb'}]}
#
# # with open('json_test', 'w+', encoding='utf-8') as fp:
# #     json.dump(json_dic, fp, ensure_ascii=False)
# print(json_dic['c'][0], type(json_dic['c'][0]))

json_dic = {'c': [{'a', 'b'}, {'bbb', 'aaa'}], 'cc': [{'aa', 'bb'}]}
str_dic =str(json_dic)
# print(str(json_dic),type(str(json_dic))
import json

# list = eval(str_dic)
# print(list, type(list))

