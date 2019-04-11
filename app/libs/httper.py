# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 13:22
# @Author  : Lwq
# @File    : httper.py
# @Software: PyCharm
import requests


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)

        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
