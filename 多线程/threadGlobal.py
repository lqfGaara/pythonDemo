from  threading import Thread
import time
#线程间贡献全局变量，进程间不共享全局变量
num=100
def work1():
    global num
    for i in range(5):
        num+=1
    print("work1执行后的num=%s"%num)

def work2():
    global num
    print("work2执行后的num=%s"%num)
print("num=%s"%num)
t1 = Thread(target=work1)
t1.start()
time.sleep(1)
t2 = Thread(target=work2)
t2.start()

