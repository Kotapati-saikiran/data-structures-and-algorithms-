def countOfSmallerOrEqualElements(arr, val):
    n = len(arr)
    #TWO POINTERS APPROACH 
    i = 0
    j = 1
    count = 0
    
    num_i = 0
    den_j = 0
    
    maximum_ratio = 0.0
    
    while i < n - 1:
        while j < n and arr[i] > (val * arr[j]):
            j += 1
            
        count += n - j
        
        if j == n:
            break
            
        current_ratio = arr[i]/arr[j]
        if maximum_ratio < current_ratio:
            maximum_ratio = current_ratio
            num_i = i
            den_j = j
        i += 1 
        
    return (count, num_i, den_j)
        
    
def search(arr, k):
    l = 0.0
    h = 1.0
    
    num_i = 0
    den_j = 0
    
    while l < h:
        mid = (l + h) / 2
        count = countOfSmallerOrEqualElements(arr, mid)
        
        if count[0] == k:
            num_i = count[1]
            den_j = count[2]
            break
        elif count[0] > k:
            h = mid
        else:
            l = mid 
    return [arr[num_i], arr[den_j]]
        

arr = [1,2,3,5]
k = 3    
print(search(arr, k))