# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月04日
"""

print('hello world\n !')         #换行
print('hello \t world!')         #\t一个制表位 四个字符的位置（可能不是四个）
print('hello\tworld!')           #三个字符，因为算上了o字符,一共四个
print('hello\r world')           #\r 回车 world将hello进行覆盖
print('hello\bworld\n')            #回退一个空格

print('http:\\www.baidu.ocm')   #/转义字符
print('http:\www.baidu.ocm')
print('http:\\\\www.baidu.ocm\n')

# print('同学们说:'老师好！'')
print('同学们说:\'老师好！\'\n')  #将需要转义的字符前加上 \

#原字符，不希望 \ 在字符串中起作用。 在字符串之前加上r或者R
print(r'hello\nworld!')
#注意，最后一个字符不可以为\
# print(r'hello\nworld\')
print(r'hello\nworld\\')


