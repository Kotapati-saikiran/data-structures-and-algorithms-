def sorted_or_not(arr,i):
    while(arr[i-1] < arr[i] and i <= len(arr)):
        return True
        i+=1
    return False
    i+=1
    
arr=[1,2,3,4,5]
i=1
res=sorted_or_not(arr,i)
print(res)

#----------------------------------------
"""arr=[1,2,3,4,5]
a=sorted(arr)
if(arr==a):
    print(True)
else:
    print(False)"""