from threading import Thread 
from time import sleep

videos = ['Python','OOPS','Multithreading','File Handling']
class MyThread(Thread):
    def run(self):
        for vid in videos:
            print(f"{vid} Started!")
            sleep(3)
            print(f"{vid} Uploaded successfully")
t1 = MyThread()
t1.start()
