# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 19:04
# @Author  : Lwq
# @File    : base.py
# @Software: PyCharm
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, SmallInteger

db = SQLAlchemy()


class Base(db.Model):
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)
