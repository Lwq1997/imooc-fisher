# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 19:03
# @Author  : Lwq
# @File    : gift.py
# @Software: PyCharm
from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash

from app.models.base import Base


class User(Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    _password = Column('password', String(64))
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)

    @property
    def password(self):
        pass

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)
