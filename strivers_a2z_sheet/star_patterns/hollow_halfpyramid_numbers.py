n=4
for i in range(n):
    for j in range(0,i+1):
        print(j+1,end=" ")
    for k in range(2*(n-i-1)):
        print(" ",end=" ")
    for l in range(i,-1,-1):
        print(l+1,end=" ")
    print()