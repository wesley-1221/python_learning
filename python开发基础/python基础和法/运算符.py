# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月04日
"""

#算数运算符 + - * /   //（整除） %（取模）  **（幂运算）
#除    一正一负向下取正
print(9 % -4)    # 商-3   余数=被除数-除数*商
print(-9 % 4)    #

#赋值运算符 =  +=  -=  *=  /=  //=  %=
a, b, c = 20, 30, 40
print(a, b, c)

#比较运算符 ==   ！=  >=  <=  >  <  结果是true，false

#布尔运算符
"""
and   （两真为真，一假则假）
or     (一真则真)
not   （取反）
"""
f = True
print(not f)

#in 与 not in   （在与不在）

#位运算和优先级
"""
位于&  ：  都真则真
位于|  ：  都假才假
左移位运算符<<  ：  高位溢出舍弃，低位补0
右移位运算符  >>：  低位溢出舍弃，高位补0  #二进制算
"""
print(4&8)
print(4|8)
print(4<<1)
print(4>>2)

#运算符优先级：




