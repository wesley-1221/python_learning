# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月14日
"""

"""
def a_new_decorator(a_func):
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction


# def a_function_requiring_decoration():
#     print("I am the function which needs some decoration to remove my foul smell")
#
#
# a_function_requiring_decoration()
# # outputs: "I am the function which needs some decoration to remove my foul smell"
# #importance
# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
# # now a_function_requiring_decoration is wrapped by wrapTheFunction()
#
# a_function_requiring_decoration()
# # outputs:I am doing some boring work before executing a_func()
# #        I am the function which needs some decoration to remove my foul smell
# #        I am doing some boring work after executing a_func()

@a_new_decorator
def a_function_requiring_decoration():
    
    print("I am the function which needs some decoration to "
          "remove my foul smell")


a_function_requiring_decoration()
# outputs: I am doing some boring work before executing a_func()
#         I am the function which needs some decoration to remove my foul smell
#         I am doing some boring work after executing a_func()

# the @a_new_decorator is just a short way of saying:
# a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)

print(a_function_requiring_decoration.__name__)            # wrapTheFunction这并不是我们想要的！Ouput输出应该是"a_function_requiring_decoration"

"""

from functools import wraps


def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction


@a_new_decorator
def a_function_requiring_decoration():
    """Hey yo! Decorate me!"""
    print("I am the function which needs some decoration to "
          "remove my foul smell")


print(a_function_requiring_decoration.__name__)
# Output: a_function_requiring_decoration

