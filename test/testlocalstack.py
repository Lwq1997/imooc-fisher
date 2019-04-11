# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 19:58
# @Author  : Lwq
# @File    : testlocalstack.py
# @Software: PyCharm
import threading
import time

from werkzeug.local import LocalStack

stack = LocalStack()
stack.push(1)
print('main thread: ' + str(stack.top))


def work():
    print('new thread: ' + str(stack.top))
    stack.push(2)
    print('new thread: ' + str(stack.top))


thread_1 = threading.Thread(target=work)
thread_1.start()
# 停留一秒是确保线程1执行完成
time.sleep(1)
print('main thread: ' + str(stack.top))
