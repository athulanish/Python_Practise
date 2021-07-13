A = [1,2,3,4]
print (A)

##To print a specific item from a list
print(3 in A)

print(A.index(3))

try:    
    print(A[3])
except IndexError:
    print("out of range")

B = [5,3,6,7]

c = [A,B]
print(c)

##To combine two lists 
D = A + B
print (D)

##To remove an element from a list
E = A.remove(3)
print(E)

print(A)

##Remove duplicates from list
sample = [1,2,3,2,3,2,4,5,2,5,3,5,6,7,7,7,4]
res = list(set(sample))
print(res)

new_sample = [2,2,2,5,4,3,4,4,4,6,5,4,5,5,6,7,5]
from collections import OrderedDict
new_res = list(OrderedDict.fromkeys(new_sample))
print(new_res)

##Remove all elements from a list 
F = [3,4,5,6,7,5,6,7,4]
print(F)
F.clear()
print(F)


##Count elements in a list
print(D)
D.count()






