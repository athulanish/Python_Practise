## A ternary operator is a simpler version of an if-else statement

a = 24
b = 35 
#get an minimum output for a if its smaller than b
print("a is minimum" if a<b else "a is maximum")

good_movie = True
print("Movie is a blockbuster" if good_movie else "Movie is a one time watch")
##lets try the above exercise using tuple method
print(("Movie is a one time watch","Movie is a blockbuster")[good_movie])

num = 13
print("Even" if num%2 == 0 else "Odd")
##using tuple method
print(("Odd", "Even")[num%2 == 0])


##Define a function for range
def ran(n):
    if n > 0:
        ran(n-1)
        print (n)

print(ran(100))



