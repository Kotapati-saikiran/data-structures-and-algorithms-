def sorted_or_not(arr):
    for i in range(1, len(arr)):
        if arr[i - 1] > arr[i]:
            return False
    return True

arr = [1, 2, 3, 4, 5]
res = sorted_or_not(arr)
print(res)

#----------------------------------------
"""arr=[1,2,3,4,5]
a=sorted(arr)
if(arr==a):
    print(True)
else:
    print(False)"""