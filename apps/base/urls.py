# -*- coding: utf8 -*-
# @Time    : 2022/6/18 18:42
# @Author  : wxvirus
# @File    : urls.py
# @Software: PyCharm
from django.urls import path
from rest_framework import routers

from .views import account

router = routers.SimpleRouter()

# 其他的注册方式
# router.register(r'comment', comment.CommentView)

urlpatterns = [
    path('auth/', account.AuthView.as_view()),
    path('test/', account.TestView.as_view()),
]

urlpatterns += router.urls
