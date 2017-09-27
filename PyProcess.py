from multiprocessing import Process
import time
# 因为fork只能在类Linux平台使用，所以要想做到跨平台，需要用Process

def test():
    for i in range (5):
        print("test process")
        time.sleep(1)
# target 传入的值就是子进程执行的目标函数，函数执行完进程结束
p=Process(target=test())
p.start()
# join 的功能是p进程执行完之后才会执行主进程的程序  ，这时候就是主线程阻塞
p.join(2)
print("main process")
