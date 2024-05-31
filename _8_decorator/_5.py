"""
用类实现的 timer 装饰器
"""

from functools import wraps
import time


class timer:
    """装饰器：打印函数耗时
    :param print_args: 是否打印方法名和参数，默认为 False
    """

    def __init__(self, print_args):
        self.print_args = print_args

    def __call__(self, func):
        @wraps(func)
        def decorated(*args, **kwargs):
            st = time.perf_counter()
            ret = func(*args, **kwargs)
            if self.print_args:
                print(f'"{func.__name__}", args: {args}, kwargs:{kwargs}')
            print('time cost: {} seconds'.format(time.perf_counter() - st))
            return ret

        return decorated
