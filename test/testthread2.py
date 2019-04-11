# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 19:59
# @Author  : Lwq
# @File    : testthread2.py
# @Software: PyCharm
import threading
import time

from werkzeug.local import Local

'''
线程有隔离
'''
test = Local()
test.a = 1


def work():
    test.a = 2
    print('new thread'+str(test.a))


thread_1 = threading.Thread(target=work)
thread_1.start()
# 停留一秒是确保线程1执行完成
time.sleep(1)
print('main thread'+str(test.a))