# coding=utf-8
# 2022年4月1日14:27:56

import time
from functools import wraps


def time_count(func):
    """
    计算程序耗时的装饰器
    :param func:
    :return:
    """
    @wraps(func)
    def use_time():
        start_time = time.time()
        func()
        end_time = time.time()
        use_t = "{:.4f}".format(end_time - start_time)
        now_func_name = func.__name__
        log_str = "{fun_n}函数耗时：{use_t}秒".format(fun_n=now_func_name, use_t=use_t)
        print(log_str)

    return use_time


@time_count
def func_test():
    for i in range(10):
        time.sleep(0.1)


if __name__ == '__main__':
    func_test()
