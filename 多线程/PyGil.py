# gil全局解释器 ，当完成多任务的时候使用多线程的时候实际上是假的多线程,在同一时刻Gil只能让一个线程工作，所以一般
# 用多进程效率更高
# 怎么解决Gil问题呢？一般我们把子线程需要完成的任务用C语言写

import threading
from ctypes import *

# 动态加载so库
looplib = cdll.LoadLibrary("./libdeadloop.so")
# 创建子线程
t1 = threading.Thread(target=looplib.loop)
t1.start()
