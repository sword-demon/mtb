# -*- coding: utf8 -*-
# @Time    : 2022/6/18 18:45
# @Author  : wxvirus
# @File    : account.py
# @Software: PyCharm
import jwt
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings

from ..serializers.account import AuthSerializer
from utils import return_code
from .. import models


class AuthView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        # 1. 获取用户请求发送的用户名和密码
        serializer = AuthSerializer(data=request.data)
        # 2. 数据校验
        if not serializer.is_valid():
            return Response({"code": return_code.VALIDATE_ERROR, "detail": serializer.errors})

        # 3. 数据库校验
        username = serializer.validated_data.get("username")
        password = serializer.validated_data.get("password")
        user_object = models.UserInfo.objects.filter(username=username, password=password).first()
        if not user_object:
            return Response({"code": return_code.AUTH_FAILED, "detail": "用户名或密码错误"})

        # 4. 生成jwt token 返回
        # 生成header
        headers = {
            'typ': 'jwt',
            'alg': 'HS256'
        }
        # 构建payload
        payload = {
            'user_id': user_object.id,
            'username': username,
            'exp': datetime.datetime.now() + datetime.timedelta(minutes=5)  # 超时时间
        }
        token = jwt.encode(payload=payload, key=settings.SECRET_KEY, algorithm="HS256", headers=headers)
        return Response({"code": return_code.SUCCESS, "data": {"token": token, "username": username}})


class TestView(APIView):

    def get(self, request, *args, **kwargs):
        print(request.user.user_id)
        print(request.user.username)
        print(request.user.exp)
        return Response({"code": return_code.SUCCESS})
