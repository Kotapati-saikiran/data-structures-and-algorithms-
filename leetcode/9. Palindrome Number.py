def palindrome(x):
    if(x<0):
        return False
    r=0
    xcopy=x
    
    while(x>0):
        r=(r*10) + (x%10)
        x//=10
        
    return r==xcopy
x=int(input())
print(palindrome(x))

#--------------------------------
''' 
0*10+1=1
12
1*10+12%10=(10+2)=12
1
12*10+1%10=(120+1)=121
'''