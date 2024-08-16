from threading import Thread 
from time import sleep
class MyThread(Thread):
    def run(self):
        self.print_message()

    def print_message(self):
        for i in range(5):
            print(f"{i}. This is user defined thread.")
            sleep(2)

myThread = MyThread()
myThread.start()
