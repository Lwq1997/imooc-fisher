# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 16:30
# @Author  : Lwq
# @File    : testthread1.py
# @Software: PyCharm
import threading
import time

'''
线程没有隔离
'''


class TestThread:
    a = 0


test = TestThread()


def work():
    test.a = 2


thread_1 = threading.Thread(target=work)
thread_1.start()
time.sleep(1)
print(test.a)
