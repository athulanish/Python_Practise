##Create a set
A = {1,2,3,4,5,6,7,8}
print(A)

## Create a set with mixed values
B = {1,'A',3,'B',5,'L'}
print(B)

##How to add duplicates to a set 
C = set([1,2,3,4,4,4,5,6,6,7])
print(C)

##Convert list to set
D = [1,'Name',2,'Jungle',3,'Rabbit']
print(D)

random = set(D)
print(random)

##Converting list containing duplicate elements to a set
D.insert(1,1)
print(D)

#Since we can add only 1 item using insert method, lets try extend
D.extend([1,1,2,2,5,6,6,7])
print(D)

random = set(D)
print (random)




