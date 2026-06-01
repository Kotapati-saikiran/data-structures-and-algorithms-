#second largest element in the array
#-------------------------------------------
arr = [1,2,4,7,7,5]

smallest = float('inf')  
second_smallest = float('inf') # 'inf' means larger than every possible number

largest = float('-inf')
second_largest = float('-inf') # 'inf' means smaller than every possible number

for num in arr:
    if num > largest:
        second_largest = largest
        largest = num
    elif largest > num > second_largest:
        second_largest = num
        
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif smallest < num < second_smallest:
        second_smallest = num
        
print(second_largest)
print(second_smallest)
#---------------------------------
"""arr = [1,2,4,7,7,5]
print(arr[1])
print(arr[len(arr)-2])"""