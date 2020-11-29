# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月15日
"""
# 高级文件，文件夹， 压缩包 处理
import shutil
import os
if not os.path.exists('./shutil_test'):
    os.mkdir('./shutil_test')
    os.chdir('./shutil_test')
    f1 = open(file="shutilTest1", mode='a', encoding='utf-8')
    f2 = open(file="shutilTest2", mode='a', encoding='utf-8')
    f1.write("learning shutil")
    f2.write("好好学习")
    f1.close()
    f2.close()
    shutil.copyfileobj(open('shutilTest1', 'r'), open('shutilTest2', 'a'))
else:
    pass