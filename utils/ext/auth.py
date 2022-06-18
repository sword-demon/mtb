# -*- coding: utf8 -*-
# @Time    : 2022/6/18 22:58
# @Author  : wxvirus
# @File    : auth.py
# @Software: PyCharm
import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings

from .. import return_code


class CurrentUser(object):
    def __init__(self, user_id, username, exp):
        self.user_id = user_id
        self.username = username
        self.exp = exp


class JwtTokenAuthentication(BaseAuthentication):

    def authenticate(self, request):
        """
        去请求头获取token
        读取用户提交的jwt token校验
        :param request:
        :return:
        """
        token = request.META.get("HTTP_AUTHORIZATION")
        if not token:
            raise AuthenticationFailed({"code": return_code.AUTH_FAILED, "error": "认证失败"})
        # jwt token 校验
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, ["HS256"])
            # print(payload)
            return CurrentUser(**payload), token
        except Exception as e:
            raise AuthenticationFailed({"code": return_code.AUTH_FAILED, "error": "认证失败"})

    def authenticate_header(self, request):
        return "Bearer realm='API'"
