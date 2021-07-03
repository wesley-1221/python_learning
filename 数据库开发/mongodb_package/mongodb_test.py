# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年12月06日
"""

import pymongo

# 创建mongodb的连接对象
client = pymongo.MongoClient(host="localhost", port=27017)
# client = MongoClient('mongodb://localhost:27017/')
print(client)

# 指定数据库
db = client.python_test
# db = client['python_test']

# 指定集合（collection）
collection = db.student
# collection = db["student"]

# 插入数据
"""
MongoDB中，每条数据其实都有一个_id属性来唯一标识。
如果没有显式指明该属性，MongoDB会自动产生一个ObjectId类型的_id属性。
insert()方法会在执行后返回_id值。
"""
# student = {
#     'id': '20170101',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }
#
# result = collection.insert(student)
# print(result)
#
# student1 = {
#     'id': '20170101',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }
# student2 = {
#     'id': '20170202',
#     'name': 'Mike',
#     'age': 21,
#     'gender': 'male'
# }
#
# result = collection.insert([student1, student2])
# print(result)

"""
PyMongo 3.x版本中，官方已经不推荐使用insert()方法了。当然，继续使用也没有什么问题。
官方推荐使用insert_one()和insert_many()方法来分别插入单条记录和多条记录
"""

# student = {
#     'id': '20170101',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }
#
# result = collection.insert_one(student)
# print(result)
# print(result.inserted_id)



