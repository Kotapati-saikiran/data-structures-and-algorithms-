arr =  [6,5,7,9,2,2]
arr.sort(reverse=True)
sum = 0
for i in range(len(arr)):
    if (i + 1) % 3 != 0: 
        sum+=arr[i]
print(sum)

#-------------------------------(second version mine first chat gpt)
"""arr =  [6,5,7,9,2,2]
arr.sort()
sum = 0
c = 0
for i in range(len(arr)-1,-1,-1):
    if(c==2):
        c=0
    else:
        sum+=arr[i]
        c+=1
print(sum)"""