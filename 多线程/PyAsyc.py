# 多线程的异步
import os
import time
from  multiprocessing import Pool


def excute():
    print("进程%s正在执行" % os.getpid())
    time.sleep(3)


def call(args):
    print("回收了进程%s的任务" % os.getpid())


pool = Pool(2)
pool.apply_async(func=excute, callback=call)
pool.close()
pool.join()
