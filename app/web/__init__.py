# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 14:20
# @Author  : Lwq
# @File    : __init__.py.py
# @Software: PyCharm
from flask import render_template, Blueprint

web = Blueprint('web',__name__)


@web.app_errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


from app.web import book
from app.web import auth
from app.web import main
from app.web import gift
from app.web import drift
from app.web import wish
