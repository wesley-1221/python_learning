# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月15日
"""

import datetime
#返回当前日期
# d = datetime.datetime.now()                    # 2020-11-15 13:42:16.288617
# print(d)
# print(d.timestamp())                           # 1605419021.135349
# print(d.today())                              # 2020-11-15 13:43:41.135350
# print(d.year)                                 # 2020
# print(d.timetuple())                          # time.struct_time(tm_year=2020, tm_mon=11, tm_mday=15, tm_hour=13, tm_min=43, tm_sec=41, tm_wday=6, tm_yday=320, tm_isdst=-1)


# 时间运算
# print(datetime.datetime.now())
# print(datetime.datetime.now()+datetime.timedelta(4))    # 当前时间加四天
# print(datetime.datetime.now()+datetime.timedelta(hours=4))    # 当前时间加四小时
"""
2020-11-15 13:47:54.568744
2020-11-19 13:47:54.569537
2020-11-15 17:47:54.569537
"""

# 时间替换
d = datetime.datetime.now()                    # 2020-11-15 13:42:16.288617
print(d)
print(d.replace(year=2999, month=5, day=5))   # 没有改变原来的时间
print(d)

















