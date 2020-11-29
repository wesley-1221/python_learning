# -*- coding:utf-8 -*-
"""
作者:wesley
日期:2020年11月29日
"""

# class MyException(BaseException): # BaseException是所有异常的基类
#     def __init__(self,msg):
#         self.message = msg
#     def __str__(self):
#         return self.message
# try:
#     raise MyException("我的错误")
# except MyException as e:
#     print(e)







class YoutubeConnectionError(BaseException):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg


name = "alex"
d = [1,2,3]

while True:
    try:
        num1 = int(input("n1>:"))
        num2 = int(input("n2>:"))

        res = num1 + num2

        print("result:",res,name)
        raise YoutubeConnectionError("在中国无法翻墙")
        #name.check
        #open("filetest")
        #d[3]

    except (KeyboardInterrupt,EOFError) as e: #强类型错误
        print(e)

    except AttributeError as e:
        print(e)
    except NameError as e :
        print(e)
    except  ValueError as err:
        print("输出的值不合法，必须是数字")

    except YoutubeConnectionError as e:
        print("error",e)
    except Exception as e:
        print("发生错误",e)

    else:
        print("没发生异常走这里")

    finally:
        print("不管有没有发生异常，都走这里。。。")
