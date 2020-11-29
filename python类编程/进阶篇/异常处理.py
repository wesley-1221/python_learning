# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月29日
"""

# s1 = 'hello'
# try:
#     #int(s1)
#     print(d)
# except IndexError as e:
#     print(e)
# except KeyError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# except Exception as e:
#     print("最后的万能异常",e)
# # 最后的万能异常 name 'd' is not defined

try:
    # 主代码块
    pass
except KeyError as e:
    # 异常时，执行该块
    pass
else:
    # 主代码块执行完，若未触发任何异常，执行该块
    pass
finally:
    # 无论监测的代码是否发生异常，都执行该处代码
    pass