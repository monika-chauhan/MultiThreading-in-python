from threading import Thread 
from time import sleep 

videos = ['Python','OOPS', 'file Hanlding','Multithreading']
class MyThread(Thread):
    def __init__(self,val,video):
        self.kid = val 
        self.video = video
        Thread.__init__(self)
    
    def upload_videos(self):
        for video in videos:
            print(f"{video} Started!")
            sleep(2)
            print(f"{video} Uploaded!")
    
    def compressed(self):
        for video in videos:
            print(f"{video} Compressed!")
    

    def run(self):
        self.upload_videos()
        self.compressed()
        if self.kid:
            print(f"{self.video} is Suitable for Kids")

t1 = MyThread(True,'Python')
t1.start()
