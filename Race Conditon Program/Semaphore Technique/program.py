from threading import Thread, Semaphore 
import time 

obj = Semaphore(3) # default = 1 
# We can use multiple acquire and release 
def display(name):
    obj.acquire() # decrement internal counter by 1 
    for i in range(5):
        print('Hello')
        print(name)
        time.sleep(1)
    obj.release() # increment internal counter by 1

t1 = Thread(target=display,args=('Thread-1',))
t2 = Thread(target=display,args=('Thread-2',))
t3 = Thread(target=display,args=('Thread-3',))
t4 = Thread(target=display,args=('Thread-4',))
t5 = Thread(target=display,args=('Thread-5',))
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
