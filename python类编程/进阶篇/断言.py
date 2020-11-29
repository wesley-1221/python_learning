# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月29日
"""

def my_interface(name,age,score):
    assert type(name) is str
    assert type(age) is int
    assert type(score) is float
my_interface("wesley",22,89.2)
my_interface("wesley",22,89)                  # AssertionError