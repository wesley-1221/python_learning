# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月15日
"""
# 1
"""
a = [1, 2, 3, 4]
# for index, item in enumerate(a):
#     a[index] += 1
# print(a)

# a = map(lambda x:x+1, a)
# for i in a:
#     print(i)
#列表生成式
# a = [i+1 for i in a]
# print(a)
"""
# 2
# # 生成器（一边生成，一边计算）
# #generator
# L = [x*x for x in range(10)]              #列表生成式
# print(L)
# # 这就是一个生成器
# g = (x*x for x in range(10))              # <generator object <genexpr> at 0x000001D14DECDD48>
# print(g)
#
# # 访问生成器
# for i in g:                                # 一直next（g），会一个一个出答案，直到没有结果抛出异常（stoplteration）,自动跳出循环
#     print(i)
#

# 3
# Fibonacci
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a+b
#         n += 1
#     return "done"
# fib(10)

# generator
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         # print(b)
#         yield b              # 遇到yield就会终中断，再次调用next（）时，继续执行上次的代码
#         a, b = b, a+b
#         n += 1
#     return "done"
# g = fib(10)
# print(g)                      # <generator object fib at 0x000001C43CDE74C8>
# # 执行流程：每次调用next（）的时候执行，遇到yield语句返回，再次被next（）调用next（）调用时从上次返回yield语句处继续执行
# # print(g.__next__())
# # print(g.__next__())
# # print("执行其它的")
# # print(g.__next__())
# # print(g.__next__())
# # """
# # 1
# # 1
# # 执行其它的
# # 2
# # 3
# # """
#
# # for n in fib(6):
# #     print(n)                     # 发现没有return值
# # 如果想拿到返回值，就要捕获错误
#
# g = fib(6)
# while True:
#     try:
#         x = next(g)
#         print(x)
#     except StopIteration as e:
#         print(e.value)
#         break
# """
# 1
# 1
# 2
# 3
# 5
# 8
# done
# """

# 4
# 实现单线程并发运算








