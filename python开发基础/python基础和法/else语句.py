# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月04日
"""

"""
if  else

#循环结束之后，没有遇到break，则执行else。遇到break则不再执行
while  else
for  else
"""

# for item in range(3):
#     pwd = input("请输入密码：\n")
#     if pwd == "8888":
#         print('输入密码正确！')
#         break
#     else:
#         print('输入密码错误')
# else:
#     print('三次密码都输入错误')

s = 0
while s < 3:
    s += 1
    pwd = input("请输入密码：\n")
    if pwd == "8888":
        print('输入密码正确！')
        break
    else:
        print('输入密码错误')
else:
    print('三次密码都输入错误')