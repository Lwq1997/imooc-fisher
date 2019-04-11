# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 21:16
# @Author  : Lwq
# @File    : fisher.py
# @Software: PyCharm
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=8088, threaded=True)
