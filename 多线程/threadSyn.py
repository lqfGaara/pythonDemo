from threading import Thread
import time

num=0
flag=0
def test1():
    global num
    global flag
    if flag==0:
        for i in range(1000000):
            num+=1
        flag=1
        print("test1=%s"%num)

def test2():
    global num
    while True:
        if flag!=0:
            for i in range(1000000):
                num+=1
            print("test2=%s"%num)
            break

t1=Thread(target=test1)
t1.start()

t2=Thread(target=test2)
t2.start()
