# -*- coding: utf-8 -*-
# @author: wesley
# @time: 2021/7/3:14:14
# @software: PyCharm

import hmac
import os

secret_key = b"wesley"
randseq = os.urandom(32)

hmac = hmac.new(secret_key, randseq)
hmac_code = hmac.digest()
print(hmac_code)                   # 得到一个字节串， 不用解码编码了




