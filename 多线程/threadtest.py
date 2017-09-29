import threading
import time
class Mythread(threading.Thread):
    def run(self):
       for i in range(5):
           time.sleep(1)
           print("-----+%s----"%i)

t=Mythread()
t.start()
