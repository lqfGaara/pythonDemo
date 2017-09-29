from threading import Thread
import time
from queue import Queue
#成产者
class Producer(Thread):
    def run(self):
        while True:
            global queue
            count=0
            if queue.qsize()<500:
                count+=1
                queue.put(self.name+"生产了%s"%count)
                print(self.name+"生产了%s"%count)
            time.sleep(1)
class Consumer(Thread):
    def run(self):
        while True:
            global queue
            count=0
            if queue.qsize()>100:
                queue.get()
                count+=1
                print(self.name+"消费了%s"%count)
            time.sleep(1)
if __name__ == "__main__":
    queue=Queue()
   #初始化生产200个
    for i in range(200):
        queue.put("产品%s号"%i)
    p=Producer()
    c=Consumer()
    p.start()
    c.start()

