# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 21:08
# @Author  : Lwq
# @File    : main.py
# @Software: PyCharm
from app.web.blueprint import web


@web.route('/')
def index():
    return "hello"
