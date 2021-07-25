import time

def yrange():
    a = [x for x in range(100000000)]
    return a

def crange(value):
    i =  0
    while i < value:
        yield i
        i += 1  


    
    


start_time = time.time()
for y in yrange():
    pass
x = time.time() - start_time
print(x)

start_time = time.time()
for c in crange(100000000):
    pass
z = time.time() - start_time
print(z)

