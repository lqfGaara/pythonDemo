from threading import Thread
import time
import threading
#多线程中函数的局部变量互相不影响
def test1():
        num=100
        name=threading.current_thread().name
        if name == "Thread-1":
            num+=1
            print("Thread=%s+num=%d"%(name,num))
        else:
            time.sleep(1)
            print("Thread=%s+num=%d"%(name,num))

t1=Thread(target=test1)
t1.start()

t2=Thread(target=test1)
t2.start()
