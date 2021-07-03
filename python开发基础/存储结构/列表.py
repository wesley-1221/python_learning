# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月04日
"""

# #创建：list ， []
# list_1 = ['hello', 'world', 99, 'hello']
# list_2 = list(['hello', 'world', 99, 'hello'])
# print(list_1,"\t",list_2)
#
# #查
# #按照值查索引
# print(list_1.index('hello'))     #多个只输出第一个
# print(list_1.index('hello', 2, 4))
# #print(list_1.index('98'))        #ValueError: 'hello' is not in list
#
# #按照索引查值
# #获取单个元素
# print(list_1[1])
# print(list_1[-3])
# # print(list_1[10])     #IndexError: list index out of range

# 获取多个元素
# 切片  [start:stop:step]     左闭右开.step不写，默认为1
# step为正数
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(lst[1:5:2])
# print(lst[1:5:1])
# print(lst[:5:1])
# print(lst[1::2])
# print("++++++++++++++++++++++++")
# #step为负数
# print(lst[::-1])
# print(lst[7::-1])          #[8, 7, 6, 5, 4, 3, 2, 1]
# print(lst[7:4:-1])

"""
#列表的判断和遍历
#判断
lst = [10,20,'python','hello']
print(10 in lst)
print(10 not in lst)

#遍历
for item in lst:
    print(item, end = '\t')
"""

#增
#lst = [10, 20, 30]
#添加一个元素
# print(lst, id(lst))
# lst.append(40)                 #[10, 20, 30, 40] 2364472512904
# print(lst, id(lst))            #还是同一个列表
# list_1 = lst.append(50)
# print(lst, id(list_1))
"""
#添加一个列表
#append
lst.append([40,50])              #[10, 20, 30, [40, 50]]
print(lst)
#extend                 #向列表的末尾加元素，而不是整个列表
lst.extend([60,70])              #[10, 20, 30, [40, 50], 60, 70]
print(lst)

#在任意位置添加
#下标为1的位置添加0，其它往后移动
lst.insert(1,0)          #[10, 0, 20, 30, [40, 50], 60, 70]
print(lst)
"""
# #添加切片
# lst = [0,1,2,3,4,5,6,7,8,9,10]
# list_1 = [True, False, 'hello']
# #把下标为1的后面全部切片掉，添加list_1的元素
# lst[1:] = list_1              #[0, True, False, 'hello']
# print(lst)

#删
#根据值移除
# lst = [0, 1, 2, 3, 4, 1]
# lst.remove(1)                #有重复元素将第一个1删掉
# #lst.remove(100)              #list.remove(x): x not in list
# print(lst)

#pop 根据索引移除元素
# lst.pop(0)
# print(lst)
# #pop 如果不指定元素，则删除最后一个元素
# lst.pop()
# print(lst)

#删除切片
#产生新列表对象
lst = [0, 1, 2, 3, 4, 1]
# #只要 lst[1:5] 中的元素 （左闭右开）
# lst_new = lst[1:5]              #[1, 2, 3, 4]   产生一个新的列表对象
# print(lst)                      #[0, 1, 2, 3, 4, 1]
# print(lst_new)
#不产生新列表对象
# lst[1:3] = []            #[0, 3, 4, 1]  在原列表中删除lst[1:3]的元素
# print(lst)
#
# #clear 清除列表中的全部元素
# lst.clear()               #[]
# print(lst)
#
# #删除列表
# del lst
# print(lst)


#改
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lst[2] = 100
print(lst)

#使用切片
lst[1:3] = [10,20,30,40]
print(lst)


#排序操作
#没有产生新的列表
list_1 = [2, 5, 4, 1, 3, 6, 5, 4]
print("排序前的列表：", list_1, id(list_1))
list_1.sort()
print("排序后的列表：", list_1, id(list_1))
#降序
list_1.sort(reverse=True)
print("降序：", list_1)

#产生新的列表
# print(id(list_1))
# lst_new = sorted(list_1)
# print(lst_new, id(lst_new))

#使用参数的降序
#sorted(list_1,reversed = True)


