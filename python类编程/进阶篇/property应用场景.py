# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月28日
"""

"""
比如 ，你想知道一个航班当前的状态，是到达了、延迟了、取消了、还是已经飞走了， 想知道这种状态你必须经历以下几步
1. 连接航空公司API查询
2. 对查询结果进行解析
3. 返回结果给你的用户
"""
# 因此这个status属性的值是一系列动作后才得到的结果，所以你每次调用时，其实它都要经过一系列的动作才返回你结果，但这些动作过程不需要用户关心， 用户只需要调用这个属性就可以


class Flight(object):
    def __init__(self, name):
        self.flight_name = name

    def checking_status(self):
        print("connecting airline company api...... ")
        print("checking flight %s status " % self.flight_name)
        return 1                       # 就是需要的状态码

    @property
    def flight_status(self):
        status = self.checking_status()                      # 用户不需要知道的过程，只需要知道飞机状态
        if status == 0:
            print("flight got canceled...")
        elif status == 1:
            print("flight is arrived...")
        elif status == 2:
            print("flight has departured already...")
        else:
            print("cannot confirm the flight status...,please check later")

    @flight_status.setter
    def flight_status(self, status):                       # 有status参数
        status_dic = {
            0: "canceled",
            1: "arrived",
            2: "departured"
        }
        print("\033[31;1mHas changed the flight status to \033[0m", status_dic.get(status))

    @flight_status.deleter
    def flight_status(self):
        print("status got removed...")

f = Flight("CA555")
f.flight_status                                               # 得到飞机状态

# 那现在我只能查询航班状态， 既然这个flight_status已经是个属性了， 那我能否给它赋值呢？
# f.flight_status = 3                                         # AttributeError: can't set attribute

f.flight_status = 2                                         # Has changed the flight status to  departured

del f.flight_status                                         # 修改不会影响最开始的那个property
print("-------------------------------")
f.flight_status                                             # 仍然是arrived




