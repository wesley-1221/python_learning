# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月15日
"""

"""
获取当前路径 os.getcwd()
判断文件或目录是否存在 os.path.exists
判断给出路径是否是文件 os.path.isfile
创建目录 os.mkdir
复制文件 shutil.copy
拼接路径 os.path.join 自动选择 \ 或 /
删除文件 os.remove
分离文件名和扩展名 os.path.splitext
"""
import os

# print(os.getcwd())                                                             # G:\python_learn\python函数编程\常用模块
# print(os.path.exists('G:\python_learn\python函数编程\常用模块'))            # True
# print(os.listdir('G:\python_learn\python函数编程\常用模块'))                # ['datetime_module.py', 'os_module.py', 'random_module.py', 'time_module.py', '模块导入练习.py']
# print(os.path.split('G:\python_learn\python函数编程\常用模块'))             # ('G:\\python_learn\\python函数编程', '常用模块')
# print(os.path.splitext('/G:/test.py'))                                       # ('/G:/test', '.py')
# print(os.path.dirname('/G:/test.py'))                                        # /G:
# print(os.path.basename('/G:/test.py'))                                       # test.py

if os.path.exists('./os_test'):
    os.stat('./os_test')
else:
    os.mkdir('os_test')
    os.chdir('./os_test')                             #进入指定目录
    with open('osTest', 'w') as fp:
        fp.write('learning os')



