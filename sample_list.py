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
print(D.__len__())

print(D.count(3))

##populate 1000 items in a list using list comprehension method
G = []
for x in range(1000):
    G.append(x * 2)
print(G)

##LIST COMPREHENSION
new_list = ["even" if x%2 == 0 else "Odd" for x in range (1000)]
print(new_list)

list_new = ["Multiple of Three" if x%3 == 0 else "multiple of five" if x%5 == 0 else "not a multiple of 3 and 5" for x in range (1000) ]
print(list_new)











