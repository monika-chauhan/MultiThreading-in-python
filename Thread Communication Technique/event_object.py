from threading import Thread, Event
from time import sleep 

e = Event() 

def task():
    print("Game is started!!") 
    sleep(3)
    e.set() 

def end():
    e.wait()
    if e.is_set():
        print("Game is End") 
   

t1 = Thread(target=task)
t2 = Thread(target=end)
t1.start()
t2.start()
