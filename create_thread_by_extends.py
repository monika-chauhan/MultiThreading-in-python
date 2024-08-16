import threading

class Employee:
    def print_message(self,n):
        for i in range(n):
            print(f"{i}. The thread created in extend way")

e1 = Employee()
t1 = threading.Thread(target=e1.print_message,args=(5,))
t1.start() 

for i in range(5):
    print(f"{i}. This is Main thread")