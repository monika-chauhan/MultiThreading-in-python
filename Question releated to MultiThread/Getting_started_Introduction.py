# Question 0: What is thread?
# Answer: A thread is a flow of execution in a computer program. Every python program has at least one thread of execution called the Main thread.
# Both processes and threads are created and managed by underlying operating system. 
# Sometimes we may need to create additional threads in our program in order to execute code concurrently.
# Unreliable output because of multiple threads called as Race condition.


################################################################
#            Thread Life cycle Stages                          #
#--------------------------------------------------------------#
#     ------------                                             #
#    | New thread |                                            #
#     ------------                                             #
#         |                                                    #
#  ----------------                  -----------------         #
# | Running Thread | ----------- >  | Blocked Thread  |        #
#  ----------------  <------------   -----------------         #
#         |                                                    #
# -------------------                                          #
#| Terminated thread |                                         #
# -------------------                                          #
################################################################

# New thread : when We create the thread 
# Running thread : When we start a thread by t1.start()
# Terminated thread: When the thread execution completed 
# Blocked Thread: When the thread is in waiting queue, thread synchornization , waiting for other thread to execute 

###########################################################################
#                                       thread.run         ------------
#                                     |------------------ |  Sleeping  |
#                                     |       |---------> |------------|
#                                     |       |            
#                                     |       |waiting for IO
#                                     |       |                           ---------------------------
#                                     |       |            ------------->| Terminated with exception |
#                                    \|/      |  exception |              ---------------------------
#  --------------                   --|-------  raise      |
# |  New Thread  | --------------> | Runnable | ------------
# | (Thread new) |                 | (stage 2)| ------------
#  --------------                   ----------   Thread    |
#                                                exit      |               --------------------
#                                                           ------------->| Terminated normaly |
#                                                                          --------------------
#
#
#



# Question 1: What is Multitasking?
# Answer: Executing Multiple tasks at the same time.  
# Example : Different Software running at same time in computer like uploading video
# download document, executing program writing notes etc.

# Question 2: What are the types in Multitasking?
# Answer : 1. Process based Multitasking
#          2. Thread based Mutlitasking

# Question 3: What is Process based Multitasking?
# Answer : Each task is an independent program / proces. Exmaple: open Vscode in one tab
# , open power point in one tab, 
# It used in Operating system level 

# Question 4: What is thread based Multutasking?
# Answer : Each task is an independent thread(separate part of the program)
# Example: In vscode ,we are writing the program in background multiple activites are 
# performed like syntax highlighter is one thread, auto suggestion  is one thread means
# in single application running multiple subprogram.  
# It is used as programmatic level. 

# Question 5: Give a Real Life example of thread?
# Answer : Suppose one teacher teaches 10 students in one batch at intial stage. After
# some day student count got increased now student count is 60. 
# teacher make 4 batches with 20 students each 
# resource    operation         time        memory 
#  t1            20              1 hr        1 hall
#  t1            20              1 hr        1 hall 
#  t1            20              1 hr        1 hall 
# ---------------------------------------------------
# 1 resouce      60 operation    3 hr        1 hall (time consuming)
#-------------------------------------------------------------
# If we are using multithreading concept : We will be using multiple resources and assign 
# the operation by dividing each resource and particular memory to perform 
# resource    operation         time        memory 
#  t1            20              1 hr        t1 hall
#  t2            20              1 hr        t2 hall 
#  t3            20              1 hr        t3 hall 
# ---------------------------------------------------
# 3 resouce      60 operation    1 hr        3 hall (memory)
# --------------------------------------------------------- 

# Question 6: What is thread?   
# Answer : A Thread is operation system object that executes instructions or program.
#  A thread is separated flow of the execution in program.
#  Thread represent task or subprogram

# Question 7: Why the multithreading is required ?
#  Answer: Scenario 1: Suppose we a caculator in which we are performing 4 operations.
#           1. Addition, 2. Subtraction , 3. Multiplication 4. Division 
# Every operation take 0.01 second to run each function if we run the function 100 time 
# then it will tak 1 second to complete the program But If 
# We are using threading then for each function we will be creating a thread and assign 
# each operation to thread in this case it will be taking the 0.25 second to execute the 
# 100 function calls it divided the operation by 25 each to thread and took 0.25 seconds.

# Scenario 2: Online Payment app 
#  If multiple user making request to transfer money if we are not  following the thread
#  then we have to wait to complete one request then it will got to second request it will 
# take more time to processed the request. 
#  If we are using multithreading concept, Then we will divided the request and executing 
# every request in parallel manner it will take less time to processed the request and no 
# need to wait to complete one request as the nature of parallel processing. 
# Diagram : 
# ---------             |-----------
# | user1 | ----------> | thread 1 |  
# ---------             |-----------              ___________
# ---------             |-----------             (___________)
# | user2 | ----------> | thread 2 | ----------> |           |
# ---------             |----------- ----------> | Database  |
# ---------             |----------- ----------> |     DB    |
# | user3 | ----------> | thread 3 | ----------> (___________)
# ---------             |-----------               
# ---------             |-----------  
# | user4 | ----------> | thread 4 |
# ---------             |-----------

# Question 8: What are the advantages of multithreading ?
# Answer : 1. Improve the performance of the software or application
#          2. Reduce response time of the website or application. 
#          3. Normal program with 1-flow(one thread) but when create program with n thread
#               then n-flow. 


# Question 9: What are the application of using threading?
# Answer: 1. Video Games: Mutliple activity perform parallelly ( like at running time we can shoot by gun)
#         2. Multi Media  Graphic 
#         3. Animation: Multiple images running and create animation
#         4. Web servers to handle large request 
#         5. Applications (standalone, Desktop, Web) -> To reduce the execution time. 


# Question 10: How can we acheive threading in python ?
# Answer : In python, threading is one module by importing this we can use threading.

# Question 11 : What is Main thread in program?
# Answer : Python Interpreter starts, If make request to OS for creating one thread,the current running 
#           thread we are calling main thread then tell to os to create new thread. 
#          Any Process have at least one default thread called as Main Thread.
#          Main Thread is created by PVM(Python virtual Machine/Interpreter)

# Question 12: How to check running/current  thread?
# Answer: threading.current_thread() -> 
# Attribute : name = threading.current_thread().name 
#             status = threading.current_thread().is_alive() -> boolean value
#             identity = threading.current_thread().ident
# output-> <_MainThread(MainThread, started 36944)> 
# Name : MainThread , Status : Started , Ident(unique indentity) : 36944

# Question 13: what are type to create threading in python ?
# Answer: There are two ways to create threading . 
#          1. Using Thread Class Module 
#          2. By extending the thead class in Child class 
# Steps to create Thread using Module: 
# 1. Import threading module (import threding)
# 2. Create a function to be execute (def fun(n):print("This is threading module"))
# 3. Create new Thread by passing target as func name and args in tuple form (t1 = threading.Thread(target=fun),args=(5,))
# 4. Start the current thread (t1.start())
# Steps to create Thread using extend Method:
#1. Import threading module (import threding)
# 2. Create a function inside class to be execute (class employe: def fun(n):print("This is extend thread ways"))
# 3. create a object of employe class (e1 = employe())
# 4. Create new Thread by passing target as func name and args in tuple form (t1 = threading.Thread(target=e1.fun),args=(5,))
# 5. Start the current thread (t1.start())

# Question 14: Can we create constructor in user define thread? 
# answer: Yes , We can create the constructor in side user define thread but we have to call the
# main Thread Constructor as well without this it will throw error. 
# class MyThread(Thread):
#   def __init__(self):
#       print("User define thread constructor")
#       Thread.__init__(self) # Main thread constuctor 

# Question 15: What is Thread Name?
# Answer : Each thread has a name.
# Naming : Thread-[%d] like -> Thread-1 , Thread-2 ,
# Name of thread is store in 'name' attribute of thread object.
# Main thread are :- Main thread

# Question 16: What is thread identifier?
# Answer : Thread identidier is a id that is assign by python interpreter and it is unique
# for every thread. It assigned After only the thread has started.
# It is stored in an instance variable-ident. 

# Question 17: What is Native Identifier? 
# Answer : Property Name: native_id (assign after the thread has started!)
# Notes : Generally , Ident and native_id are same. 

# Question 18: What is PID(process id)?
# Answer : It is checked by os.getpid() as it is assigned by operation system.

# Question 19: How can we count the current running thread?
# Answer : using active_count() get the count of  running thread. 

# Question 20: What are built-in function of thread to check the details?
# Answer : 1.is_alive()     :-> Thread is running or not 
#          2.main_thread()  :-> Details of main thread 
#          3.active_count() :-> number of running thread
#          4.enumerate()    :-> List of all running thread
#          5.get_native_id():-> Know native id of thread

# Question 21: What is the join method in thread?
# Answer : If a thread wants to wait for some other thread to complete then we should implement 
#   join method. 
# t1 = Thread(target=display)
# t2 = Thread(target=display)
# t1.start()
# t2.start()
# t1.join() # make sure when t1 not finish wait t2
# t2.join() # naje sure after this thread waid for to complete thread t2















