# Question1: What do you mean by Race conditon ?
# Answer: A bug in concurrency programming is called race condition. 
# Example: We use a variable value and perform different operation on this using thread to execute
# due to which we will be getting unreliable output at some point of execution. This condition is
# called race. 
# variable x = 5 
# t1 = thread(target=add,args=(5,))
# t2 = thread(target=sub, args=(5,))
# when t1 = (x+10)  |  t2=(x-20) 
# x=100             |  x = 100
# x= 100 + 10 = 110 |  x = 110 - 20 = 90 (unreliable output) It should be x=100-20=80

# Question 2: What are steps to performed while doing operation due to which occur race.
# Answer: 1. Read teh current value of the variable 
#         2. Calculate a new value for the variable
#         3. Write new value for the variable 

# Question 3: Give real world example for Race condition?
# Answer : Bus ticket System: 
# scenario: Two users trying to book the seat in bus from website. 
# User1: Avaialble seat : 2 , User2 : Avaialble seat : 2
# one case: (It create race condition)
# make request: 2 confirm, user 2: It should be updated but still showing  Avaialble seat : 2(unreliable output)
# Other case:  
# make request: 2 confirm, user 2: Avaialble seat : 0


# Question 3: Definition of Race conditon?
# Answer : If is a bug generated when you do multiprocessing I occurs beacuse two or more thread
# tries to update the same variable and result into unreliable output. 
# concurrent access to shared resources can lead to reac conditon. 

# Question 4: How can we avoid race condition?
# Answer: Using thread synchronization technique we can avoid the race conditon. 
# Thread synchronization technique: A common approach is to protect the critical sector of code. 
# 1. Lock method : Acquire the lock in one function then release it at end of the program. It is restrict to avoid the race condition.
# 2. R-Lock method : We can acquire lock multiple time. It will not throw error. but in lock when use multiple acquire it throw error
# 3. Semaphore : Multiple thread can execute (max is 3 resources) Like(in result website the limit set 100 student can see result if 101 result made a request it will put in waiting queue once one resource release the lock then 101 will enter)
# 4. Bounded Semaphore : 

# Question 5: What is thread synchronization ?
# Answer : Thread synchronization is defined as a mechanism which ensures that two or more concurrent threads do not 
# simultaneously execute some particular program segment known as critical section.

# Question 5: What are steps to apply Lock module?
# Answer: 1. Create an Object of Lock class:-> myLock = Lock ()
#         2. Acquire Lock using :-> myLock.acquire()
#         3. Release Lock using :-> myLock.release()
# Acquire Method :-> 1.Change the state of code to locked.
#                    2.Other threads have to wait until lock is released by current working thread.
# Syntax:-> lock_object.acquire(blocking=[True],timeout=-1) 
# blocking is by default is True and timeout = -1 means until the lock will not release it is waiting in queue. 


# Question 6: Why we need RLocks in Python?
# Answer: You can not acquire lock multiple times using Lock mechanism. So We come up with R-Lock Machanism.
# -By using RLock, you can acquire() lock multiple times. 
# -Rlock is just a modified version of Lock.
# Steps: 1. Creating an object of RLock class:-> 
# from threading import RLock 
# rlock = RLock() 
# 2. Acquire lock using acquire():-> rlock.acquire()
# 3. Release lock using release() :-> rlock.release()
#It keep current running thread details

# Question 7: Why we need Semaphore?
# Answer : InLock and RLock, at a time only one Thread is allowed to execute. but sometimes our requirements is to execute
# a particular number of Thread at a time.
# Real Example : As Student result website : When student try to see the result we run the parallel thread we limit the thread as 100 then
# 100 student access the resource,
#  Semaphore can be used to limit the access to the shared resources with minited capacity.
# Steps: 1. Create an object of Semaphore class
# from threading import Semaphore 
# s = Semaphore()
# 2. Acquire lock using acquire():-> s.acquire()
# 3. Release lock using release():-> s.release()

# Question 8: How the semaphore work internally?
# Answer: Semaphore uses a internal counter to count the lock and release. When the thread acquire- in this case the counter value 
# decrease by 1 and if the thread release then increment by 1. 
# Note: We can not avoid the Race Condition using semaphore if we are not using default value as 1.

# Question 9: Where we need to use the Bounded Semaphore?
# Answer : If We use one time acquire and two time release this scenario affact the internal counter value due to which 
# it will crash the program to avoid  this  we will be using BoundedSemaphone. It will handle this scenior internally. 







