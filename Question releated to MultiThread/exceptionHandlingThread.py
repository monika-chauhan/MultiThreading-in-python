# Question 1: What will happend when exceptions occur in one thread? will it impacet other threads?
# Answer : It will throw the error but other thread will be running. To avoid the exception we can use trya nd catch block and 
# excepthook module in threading module.

# Question 2: What happens for exception in thread?
# Answer : The interpreter calles the threading.excepthook() with one argument i.e. named tuple with 4 arguments. 
# 1. the exception class (DivisionError)
# 2. exception instance/value ( Exception Message)
# 3. a traceback object  (From which function come the Exception)
# 4. Thread name ( In which thread exception occur)

# Architecture of Exception :
##################################################################
#  -----------------               ------------------            #
# | For main Thread |   --------> | sys.excepthook() |           #
#  -----------------               ------------------            #
#                                                                #
# --------------------              ----------------------       #
#| For created Thread | ---------> | threading.excepthook |      #
# --------------------              ----------------------       #
#                                            |                   #
#                                            |                   #
#                                   ----------------             #
#                                  | sys.excepthook |            #
#                                   ----------------             #
##################################################################



