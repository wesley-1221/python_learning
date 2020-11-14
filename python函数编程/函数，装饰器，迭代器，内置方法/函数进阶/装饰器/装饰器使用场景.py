# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月14日
"""
#授权
# from functools import wraps
#
#
# def requires_auth(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         auth = request.authorization
#         if not auth or not check_auth(auth.username, auth.password):
#             authenticate()
#         return f(*args, **kwargs)
#
#     return decorated


#日志
from functools import wraps


def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging


@logit
def addition_func(x):
    """Do some math."""
    return x + x


result = addition_func(4)
# Output: addition_func was called