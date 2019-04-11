# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 15:54
# @Author  : Lwq
# @File    : testwith.py
# @Software: PyCharm


class MyResource:
    def __enter__(self):
        print('连接资源')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb:
            print('有异常')
        else:
            print('没有异常')
        print('释放连接')
        # 返回True说明不把异常抛出去，默认Flase

    @staticmethod
    def query():
        print('查询操作')


try:
    with MyResource() as resource:
        1 / 0
        resource.query()
except Exception as e:
    print(e)
