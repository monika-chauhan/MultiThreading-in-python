from threading import Thread,current_thread, Lock
from time import sleep

lock = Lock()
class Bus:
    def __init__(self,name,seats):
        self.seats = seats 
        self.name = name
        self.lock = lock
    def reverse(self,need_seats):
        print(self.lock)
        self.lock.acquire()
        if self.seats >= need_seats:
            user_name = current_thread().name
            print(f"{need_seats} booked by {user_name}")
            self.seats -= need_seats
            print(f"Available Seats: {self.seats}")
        else:
            print("Sorry! seats are not available")
        self.lock.release()
        
b1 = Bus('Laxmi Travel',2)
t1 = Thread(target=b1.reverse, args =(1,),name = "Jay")
t2 = Thread(target=b1.reverse,args=(2,),name = "Raj")
t1.start()
t2.start()

