from threading import Thread
from time import sleep 

class MyThread(Thread):
    def run(self):
        a = 15 
        b = 19 
        self.temp = a + b 

t1 = MyThread()
t1.start()
print("Return the value",t1.temp)
