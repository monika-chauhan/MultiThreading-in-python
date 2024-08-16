from threading import Thread 

class Employee:
    @staticmethod
    def print_message(n):
        for i in range(n):
            print(f"{i}.This is static method in threading")

e1 = Employee()
t1 = Thread(target=e1.print_message,args=(5,))
t1.start() 

for i in range(5):
    print(f"{i}. This is Main Thread")