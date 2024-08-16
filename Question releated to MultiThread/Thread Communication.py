# Question 1: What is Thread communication ?
# Answer : In concurrent programming, sometimes we need to co-ordinate threads/.
#        : Threads communication with each other via signals.
# Thread ways to comminucate: 
#  1. Event Object 
#  2. Condition object
#  3. Queue object

# Question 2: How can we work with event object? 
# Answer : We can establish the communication between two threads only. 
# Steps : 1. create an event object. 
# 2. Create two threads which will communicate. 
# 3. Put t2 thread in waiting by using wait() method untill the t1 thread did not send the signal. 
# 4. Use set() metjod in/after t1 threads code. 

# Question 3: Built-in method in Event object?
# Answer : 1. set() : Set the internal flag to true.If flag is True, waiting thread is awakened.
#          2. reset() : Reset the internal flag to False.  
#          3. is_set() : Return True if and only if the internal flag is True.
#               example : if event.is_set(): do something(t2 code)
#          4. wait([timeout]) : Calling this function keep other thread on wait until the flag is set to True. 
#               (timeout) -> no of second , by default is -1 means until the thread  not completed wait the other thread.
        
# Question 4: What is Condition object thread communication?
# Answer : 
