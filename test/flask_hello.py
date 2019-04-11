# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 21:16
# @Author  : Lwq
# @File    : fisher.py
# @Software: PyCharm
from flask import Flask, make_response

app = Flask(__name__)
app.config.from_object('config')


@app.route('/hello/')
def hello():
    return 'hello lwq'


@app.route('/helloflask/')
def hello_flask():
    headers = {
        'content-type': 'text/plain',
        'location': 'https://www.baidu.com'
    }
    response = make_response('<html></html>', 301)
    response.headers = headers
    return response


def world():
    return 'world lwq'


app.add_url_rule('/world', view_func=world)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
