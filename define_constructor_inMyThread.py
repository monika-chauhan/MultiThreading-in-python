from threading import Thread
from time import sleep 

videos = ['Python', 'OPPS', 'File Handling','Multithreading']
class MyThread(Thread):
    def __init__(self):
        print("My thread Constructor")
        Thread.__init__(self) # We have to call the Thread Class constructor without this it will throw error
    
    def run(self):
        for vid in videos:
            print(f"{vid} Started!")
            sleep(3)
            print(f"{vid} Uploaded!")

t1 = MyThread()
t1.start()
