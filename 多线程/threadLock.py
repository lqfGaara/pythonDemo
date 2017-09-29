from threading import Thread,Lock
import time
num=0
def test1():
        global num
       #这个锁和test2所在的线程抢锁，如果一方已经成功锁上，那么另一方会阻塞，
       #一直等到这个锁被解开为止 
       #上锁  
        mutex.acquire()
        for i in range(1000000):
            num+=1
        flag=1
       #解锁
        mutex.release() 
        print("test1=%s"%num)

def test2():
            global num
            mutex.acquire()
            for i in range(1000000):
                num+=1
            mutex.release() 
            print("test2=%s"%num)
#创建一把互斥锁
mutex=Lock()
t1=Thread(target=test1)
t1.start()

t2=Thread(target=test2)
t2.start()
