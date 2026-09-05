n=5
a=65
for i in range(n):
    for j in range(i+1):
        print(chr(a+j),end=" ")
        a*=1
    print()