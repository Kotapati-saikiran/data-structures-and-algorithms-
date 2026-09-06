n=5
a=65
for i in range(n):
    for j in range(i,n):
        print(chr(a),end=" ")
        a+=1
    a=65
    print()

#------------------------------------
"""n=5
for i in range(n):
    for j in range(n-i):
        print(chr(65+j),end=" ")
    print()"""