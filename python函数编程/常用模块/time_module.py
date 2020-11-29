# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月15日
"""

# time 时间戳
import time
# 当前时间，参数可以转换时区
print(time.localtime())              #time.struct_time(tm_year=2020, tm_mon=11, tm_mday=15, tm_hour=13, tm_min=37, tm_sec=21, tm_wday=6, tm_yday=320, tm_isdst=0)
# 返回当前时间戳
print(time.time())                   #1605418730.115922
# 线程退出执行
time.sleep(2)                        #退出两秒执行
#