from threading import Thread,current_thread, RLock
from time import sleep

rlock = RLock()
class Bus:
    def __init__(self,name,seats):
        self.seats = seats 
        self.name = name
        self.rlock = rlock
    def reverse(self,need_seats):
        
        self.rlock.acquire()
        self.rlock.acquire()
        print(self.rlock)
        if self.seats >= need_seats:
            user_name = current_thread().name
            print(f"{need_seats} booked by {user_name}")
            self.seats -= need_seats
            print(f"Available Seats: {self.seats}")
        else:
            print("Sorry! seats are not available")
        self.rlock.release()
        self.rlock.release()
        
b1 = Bus('Laxmi Travel',2)
t1 = Thread(target=b1.reverse, args =(1,),name = "Jay")
t2 = Thread(target=b1.reverse,args=(2,),name = "Raj")
t1.start()
t2.start()


