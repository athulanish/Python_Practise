##Lets create a tuple 
A = 1,2,3,4
print(A)

B = (1,2,4,4,5,6)
print(B)

C = (1,)
print(C)

D = ('Name', 'Age', 'Animal', 4,5,2,1)
print(D)

##Index in tuple

print(A.index(2))

a,b,c,d,e,f = B
print(a,b,c,d,e,f)

##Add an item in tuple
J = A + B
print(J)

##how to convert tuple to string
L = str(D)
print(type(L))

##Find the count of repeated items
print(J.count(2))
print(J.count(4))

##How to remove an element from a tuple
##Since tuples are immutable, we need to convert it into a list first, remove the item and convert it back to tuple
tuple_new = ('a',1,2,5,4,4,'this needs to be removed',6)
print(tuple_new)

list_new = list(tuple_new)
print(type(list_new))
print(list_new)

list_new.remove('this needs to be removed')
print(list_new)

tuple_new = tuple(list_new)
print(tuple_new)


