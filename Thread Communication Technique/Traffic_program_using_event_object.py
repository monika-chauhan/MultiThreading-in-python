from threading import Thread, Event 
from time import sleep

e = Event() 

def light_switch():
    while True:
        print("Light is Green")
        e.set()
        sleep(5)
        print("Light is red")
        e.clear()
        sleep(5)
        e.set()
        e.exit()
        


def traffic_meesage():
    e.wait()
    while e.is_set():
        print("You can Go!") 
        sleep(0.5)
        e.wait()
    
   

t1 = Thread(target=light_switch)
t2 = Thread(target=traffic_meesage)
t1.start()
t2.start()