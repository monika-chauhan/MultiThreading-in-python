import threading

# executed by new thread 
def print_hello(n):
    for i in range(n):
        print(f"{i}. Welcome to Multithreading concept")

t1 = threading.Thread(target=print_hello, args=(5,))
t1.start()

# executed by main thread 
for i in range(5):
    print(f"{i}.This is Main thread")
