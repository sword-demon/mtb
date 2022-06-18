# -*- coding: utf8 -*-
# @Time    : 2022/6/18 18:29
# @Author  : wxvirus
# @File    : create_users.py
# @Software: PyCharm
import os
import sys
import django

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

# 找到当前系统的配置文件
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'mtb.settings')
# 启动django
django.setup()

from apps.base import models

models.UserInfo.objects.create(
    username='wujie',
    password='123123'
)
