import time
import threading

def func():
    #print("this is a sample line")
    time.sleep(4)
    #print("Waited for 4 sec")
    
start_time = time.time()


for i in range(3):
   x = threading.Thread(target=func)
   x.start()
end_time = time.time()

print (end_time - start_time)


start_time2 = time.time()
for i in range (3):
    func()
end_time2 = time.time()

print (end_time2 - start_time2)


