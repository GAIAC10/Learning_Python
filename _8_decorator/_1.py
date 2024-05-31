"""
打印函数耗时的无参数装饰器 timer
"""

import time
import random


def timer(func):
    """装饰器：打印函数耗时"""

    # decorated包装函数
    def decorated(*args, **kwargs):
        st = time.perf_counter()
        ret = func(*args, **kwargs)
        print('time cost: {} seconds'.format(time.perf_counter() - st))
        return ret

    return decorated


@timer
def random_sleep():
    """随机睡眠一小会儿"""
    time.sleep(random.random())


random_sleep()
