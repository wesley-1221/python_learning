# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月29日
"""

# isinstance(obj, cls)
# 检查obj是否是类 cls 的对象

class Foo(object):
    pass
obj = Foo()
print(isinstance(obj, Foo))             # True

# issubclass(sub,super)
# 检查sub类是否是 super 类的派生类

class Foo(object):
    pass
class Bar(Foo):
    pass
print(issubclass(Bar, Foo))             # True

