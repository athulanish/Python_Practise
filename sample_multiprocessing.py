import time
import multiprocessing

def box():
    print("This is it")
    time.sleep(5)



start_time = time.time()

for i in range (4):
    a = multiprocessing.Process(target=box)
    a.start()
end_time = time.time()
print(end_time - start_time)





    




