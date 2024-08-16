import threading 

print(threading.current_thread())
print("Current thread Name :", threading.current_thread().name)
print("Current thread running status: ", threading.current_thread().is_alive())
print("Current thread identity :" ,threading.current_thread().ident)