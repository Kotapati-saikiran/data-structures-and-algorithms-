n=5
for i in range(n):
    for j in range(0,i+1):
        print("*",end=" ")
    print()

for l in range(i-1,-1,-1):
    for j in range(0,l+1):
        print("*",end=" ")
    print()