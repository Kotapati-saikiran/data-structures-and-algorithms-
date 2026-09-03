n=5
for i in range(n):
    for k in range(0,i):
        print(" ",end=" ")
    for j in range(2*n-(2*i+1)):
        print("*",end=" ")
    print()

#--------------------------------
"""n = 5
stars = 2*n - 1 
for i in range(n):
    for k in range(i):
        print(" ", end=" ")
    for j in range(stars):
        print("*", end=" ")
    stars -= 2  
    print()"""