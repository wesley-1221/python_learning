# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月15日
"""

"""
我们把对象(变量)从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling

序列化：
持久保存状态：  在断电或重启程序之前将程序当前内存中所有的数据都保存下来（保存到文件中），
               以便于下次程序执行能够从文件中载入之前的数据，然后继续执行，这就是序列化
             
跨平台数据交互：序列化之后，不仅可以把序列化后的内容写入磁盘，还可以通过网络传输到别的机器上，
               如果收发的双方约定好实用一种序列化的格式，那么便打破了平台/语言差异化带来的限制，实现了跨平台数据交互。
"""


"""
# JSON的数据格式其实就是python里面的字典格式，里面可以包含方括号括起来的数组，也就是python里面的列表。
# Json 模块提供了四个方法： dumps、dump、loads、load

dumps和dump 序列化方法
序列化成字符串：json.dumps(json_obj)
序列化字符串到文件中：json.dump(json_obj, write_file)


pickle 模块提供了四个方法： dumps、dump、loads、load

dumps和dump 序列化方法
序列化成字符串：json.dumps(json_obj)
序列化字符串到文件中：json.dump(json_obj, write_file)
"""