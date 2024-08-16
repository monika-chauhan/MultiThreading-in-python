from threading import Thread, Lock
from time import sleep

lock = Lock()

def display(n,val):
    lock.acquire()
    for i in range(n):
        print(f"{i}. This is Display function : {val+i}")
    sleep(3)
    lock.release()

def show_number(n,val):
    lock.acquire()
    for i in range(n):
        print(f"{i}.This is number showing: {val - i}")
    lock.release()

t1 = Thread(target=display,args=(5,5))
t2 = Thread(target=show_number, args= (5,5))
t1.start()
t2.start()

