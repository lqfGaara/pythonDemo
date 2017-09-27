import os
import time

# fork 会生成子进程，主进程的pid>0,子进程的pid=0
ret = os.fork()
g_num=100
if ret == 0:
    while True:
        g_num+=1
        print(g_num)
        time.sleep(5)
else:
    while True:
        print(g_num)
        time.sleep(10)
# 两个进程之间的变量值不受影响

# while True:  fork()炸弹 执行后电脑会崩溃的
#      os.fork()