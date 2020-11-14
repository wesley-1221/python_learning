# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月14日
"""

# @wraps相当于
# def Wraps(fWrap):
#     def TmpWraps(func):
#         def WrapsDecorator(*args, **kwargs):
#             WrapsDecorator.__name__=fWrap.__name__
#             WrapsDecorator.__doc__=fWrap.__doc__
#             return func(*args, **kwargs)
#         return WrapsDecorator
#     return TmpWraps

def Wraps(fWrap):
    def TmpWraps(func):
        def WrapsDecorator(*args, **kwargs):
            WrapsDecorator.__name__=fWrap.__name__
            WrapsDecorator.__doc__=fWrap.__doc__
            return func(*args, **kwargs)
        return WrapsDecorator
    return TmpWraps


def NewDecorator(level):
    def TmpDecorator(func):
        def anotherFunc():
            '''it's another function'''
            pass
        #from functools import wraps
        #@wraps(anotherFunc)
        @Wraps(anotherFunc)
        def NewFibonacci(*args, **kwargs):
            print('[%s]func: %s is called, %s'%(level,func.__name__,NewFibonacci.__doc__))
            from time import time
            start = time()
            rst=func(*args, **kwargs)
            end=time()
            print('cost time: %.2fs'%(end-start))
            return rst
        return NewFibonacci
    return TmpDecorator


@NewDecorator('log')
def Fibonacci_print(num=10):
    if num <= 0:
        return
    minNum,maxNum=0,1
    while num > 0:
        tmpNum=minNum
        print(tmpNum, end=',')
        minNum=maxNum
        maxNum+=tmpNum
        num-=1

Fibonacci_print()
print(Fibonacci_print.__name__)