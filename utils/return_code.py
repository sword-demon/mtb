# -*- coding: utf8 -*-
# @Time    : 2022/6/18 19:01
# @Author  : wxvirus
# @File    : return_code.py
# @Software: PyCharm

# 成功
SUCCESS = 0

# 用户提交数据校验失败
VALIDATE_ERROR = 1001

# 认证失败
AUTH_FAILED = 2000

# 认证过期
AUTH_OVERDUE = 2001

# 无权访问
PERMISSION_DENIED = 3000

# 太多访问
TOO_MANY_REQUESTS = 4000
