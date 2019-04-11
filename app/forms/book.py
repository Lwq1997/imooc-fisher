# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 21:07
# @Author  : Lwq
# @File    : book.py
# @Software: PyCharm
from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    q = StringField(validators=[DataRequired(), Length(min=1, max=30, message='参数长度在1-30之间')])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)
