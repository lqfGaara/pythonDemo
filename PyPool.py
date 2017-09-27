from  multiprocessing import Pool
import time

def worktest():
    print("线程池在努力的work")
    time.sleep(1)
# 线程池创建3个线程
p=Pool(3)
for i in range(5):
    p.apply_async(worktest())
    # p.appl.(worktest())  阻塞的形式一般不用，上面的是非阻塞的形式
#关闭进程池，补在接收新的
p.close()
p.join()
print("over")