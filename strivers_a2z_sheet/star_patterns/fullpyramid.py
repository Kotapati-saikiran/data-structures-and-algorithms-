n=5
for i in range(n):
    for j in range(0,n-i-1):
        print(" ",end=" ")
    for k in range(2*i+1):
        print("*",end=" ")
    print()

for l in range(i-1,-1,-1):
    for m in range(0,n-l-1):
        print(" ",end=" ")
    for o in range(2*l+1):
        print("*",end=" ")
    print()

#-------------------------------------(clean code )
"""n = 5
for m in range(2*n - 1):
    if m < n:
        i = m
    else:
        i = 2*n - m - 2
    for j in range(n - i - 1):
        print(" ", end=" ")
    for k in range(2*i + 1):
        print("*", end=" ")
    print()"""