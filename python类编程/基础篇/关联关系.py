# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月28日
"""

# 男女朋友关系
# 1

# class Peopel(object):
#
#     def __init__(self, name, sex, age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#         self.partner = None                   # 另一半是一个对象
#
#     def do_private_shuff(self):             # self, 实例本身
#         print("我是[%s], 我的对象是[%s]" % (self.name, self.partner.name))
#
# # 如何使这两个人关联起来呢
# p1 = Peopel('李某', '男', 18)
# p2 = Peopel('毛某', '女', 8)
#
# # 再创建一个实例变量 partner
# # 双向关联
# # 这种方法必须双向关联
# p1.partner = p2
# p2.partner = p1
#
# p1.do_private_shuff()               # self 就是 p1
# p2.do_private_shuff()



# 上面那种方法不通用
# 实现只用调用一方就直接关联起来
# 2

# class relationship(object):
#
#     def __init__(self, obj1, obj2):       # 传入两个对象
#         self.couple = [obj1, obj2]
#
#     def get_couple(self, obj):
#         for i in self.couple:
#             if i != obj:
#                 print("我是%s ，我的女朋友是%s"%(obj.name, i.name))
#                 break
#         else:
#             print("你没有女朋友")
#
# class Peopel(object):
#
#     def __init__(self, name, sex, age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#     def do_private_shuff(self):             # self, 实例本身
#         pass
#
# # 如何使这两个人关联起来呢
# p1 = Peopel('李某', '男', 18)
# p2 = Peopel('毛某', '女', 8)
#
# relation_obj = relationship(p1, p2)
# print(relation_obj.couple)                     # 有两个对象[<__main__.Peopel object at 0x000002668E8C2CC8>, <__main__.Peopel object at 0x000002668E8C2DC8>]
#
# relation_obj.get_couple(p1)
# relation_obj.get_couple(p2)


# 3
# 实现对象也可以查看自己的对象

# class relationship(object):
#
#     def __init__(self):       # 传入两个对象
#         self.couple = []
#
#     def make_couple(self, obj1, obj2):
#         self.couple.append(obj1)
#         self.couple.append(obj2)
#         print("[%s] 和 [%s] 正式结为对象..." % (obj1.name, obj2.name))
#
#     def get_couple(self, obj):
#         for i in self.couple:
#             if i != obj:
#                 print("我是%s ，我的女朋友是%s"%(obj.name, i.name))
#                 break
#         else:
#             print("你没有女朋友")
#
#     def break_up(self):
#         print("正式分手！")
#         self.couple.clear()
#
# class Peopel(object):
#
#     def __init__(self, name, sex, age):
#         self.name = name
#         self.sex = sex
#         self.age = age
#
#     def do_private_shuff(self):             # self, 实例本身
#         pass
#
# # 没有对象名之前
# relation_obj = relationship()
#
# # 如何使这两个人关联起来呢
# p1 = Peopel('李某', '男', 18)
# p2 = Peopel('毛某', '女', 8)
# # 关联
# relation_obj.make_couple(p1, p2)
# # 查询
# relation_obj.get_couple(p1)
# # print(relation_obj.get_couple(p2))
# # 分手
# relation_obj.break_up()
# relation_obj.get_couple(p1)                # 解除关系之后就找不到对象了


# 实现对象也可以调用，实现relationship里面的功能
class relationship(object):

    def __init__(self):       # 传入两个对象
        self.couple = []

    def make_couple(self, obj1, obj2):
        self.couple.append(obj1)
        self.couple.append(obj2)
        print("[%s] 和 [%s] 正式结为对象..." % (obj1.name, obj2.name))

    def get_couple(self, obj):
        for i in self.couple:
            if i != obj:
                print("我是%s ，我的女朋友是%s"%(obj.name, i.name))
                break
        else:
            print("你没有女朋友")

    def break_up(self):
        print("正式分手！")
        self.couple.clear()

class Peopel(object):

    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = age
        self.relation = relation_obj          # 传入一个对象

    def do_private_shuff(self):             # self, 实例本身
        pass

# 没有对象名之前
relation_obj = relationship()

# 如何使这两个人关联起来呢
p1 = Peopel('李某', '男', 18)
p2 = Peopel('毛某', '女', 8)
# 关联
relation_obj.make_couple(p1, p2)
# 查询
relation_obj.get_couple(p1)
p1.relation.get_couple(p2)                 # 我是毛某 ，我的女朋友是李某 同样可以调用
# 分手
relation_obj.break_up()
relation_obj.get_couple(p1)                # 解除关系之后就找不到对象了






