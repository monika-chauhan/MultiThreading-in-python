from threading import Thread 
from time import sleep,time

def display(n):
    for i in range(n):
        print(f"{i}. This is thread function")
def show():
    for i in range(5):
        print("This is thread function")


    
begin_time = time()
t1 = Thread(target=display,args=(5,))
t2 = Thread(target=show)
t1.start()
t2.start()
t1.join()
t2.join()
print("The time taken by thread", time()-begin_time)

##### 
print("Normal flow")
begin_time = time()
def display(n):
    for i in range(n):
        print(f"{i}.This is Normal flow")
    
def show():
    for i in range(5):
        print("This is thread function")
display(5)
show()
print("The time in normal flow",time()-begin_time)
