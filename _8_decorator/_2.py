"""
增加 print_args 的有参数装饰器 timer
"""

import time


def timer(print_args=False):
    """装饰器：打印函数耗时

    :param print_args: 是否打印被方法名和参数，默认为 False
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            st = time.perf_counter()
            ret = func(*args, **kwargs)
            if print_args:
                print(f'"{func.__name__}", args: {args}, kwargs: {kwargs}')
            print('time cost: {} seconds'.format(time.perf_counter() - st))
            return ret

        return wrapper

    return decorator


@timer(print_args=True)
def random_sleep():
    print('test')


random_sleep()
"""
test
"random_sleep", args: (), kwargs: {}
time cost: 1.889999999999531e-05 seconds
"""
print(random_sleep.__name__)
"""
wrapper
"""
print(random_sleep.__doc__)
"""
None
"""
