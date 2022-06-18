# -*- coding: utf8 -*-
# @Time    : 2022/6/18 18:58
# @Author  : wxvirus
# @File    : account.py
# @Software: PyCharm
from rest_framework import serializers
# from rest_framework.exceptions import ValidationError
# from .. import models


class AuthSerializer(serializers.Serializer):
    username = serializers.CharField(label='用户名', required=True)
    password = serializers.CharField(label='密码', required=True, min_length=6)
