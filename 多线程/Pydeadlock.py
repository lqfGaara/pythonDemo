import threading
import time
class Mythread1(threading.Thread):
    def run(self):
       if lock1.acquire(timeout=2):
           print(self.name+"已上锁")
           time.sleep(1)
           if lock2.acquire(timeout=2):
               print(self.name+"已上锁")
               lock2.release()
           lock1.release()

class Mythread2(threading.Thread):
    def run(self):
       if lock2.acquire(timeout=3):
           print(self.name+"已上锁")
           time.sleep(1)
           if lock1.acquire(timeout=4):
               print(self.name+"已上锁")
               lock1.release()
           lock2.release()

lock1=threading.Lock()
lock2=threading.Lock()
#死锁的形成就是因为两个线程互相抢锁，但是锁都没有被释放，所以两个线程都在等
#这样两个线程都不能执行就形成了死锁。
if __name__ =="__main__":
    t1=Mythread1()
    t2=Mythread2()
    t1.start()
    t2.start()
