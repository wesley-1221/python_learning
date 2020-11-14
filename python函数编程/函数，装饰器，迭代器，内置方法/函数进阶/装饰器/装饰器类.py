# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月14日
"""
"""
现在我们有了能用于正式环境的logit装饰器，但当我们的应用的某些部分还比较脆弱时，
异常也许是需要更紧急关注的事情。比方说有时你只想打日志到一个文件。而有时你想把
引起你注意的问题发送到一个email，同时也保留日志，留个记录。这是一个使用继承的场景，
但目前为止我们只看到过用来构建装饰器的函数。
"""
from functools import wraps


class logit(object):
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile并写入
            with open(self.logfile, 'a') as opened_file:
                # 现在将日志打到指定的文件
                opened_file.write(log_string + '\n')
            # 现在，发送一个通知
            self.notify()
            return func(*args, **kwargs)

        return wrapped_function

    def notify(self):
        # logit只打日志，不做别的
        pass

# # 现在，我们给 logit 创建子类，来添加 email 的功能(虽然 email 这个话题不会在这里展开)。
# class email_logit(logit):
#
#     # 一个logit的实现版本，可以在函数调用时发送email给管理员
#
#
#     def __init__(self, email='admin@myproject.com', *args, **kwargs):
#         self.email = email
#         super(email_logit, self).__init__(*args, **kwargs)
#
#     def notify(self):
#         # 发送一封email到self.email
#         # 这里就不做实现了
#         pass