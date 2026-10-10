def search(nums, k):
    n = len(nums)
    i = 0
    j = 0
    zero_count = 0 
    best_answer = 0
    
    while j <= n - 1:
        if nums[j] == 0:
            zero_count += 1
            
        if zero_count <= k:
            j += 1
            
        elif zero_count > k:
            while zero_count > k:
                if nums[i] == 0:
                    zero_count -= 1
                i += 1
            j += 1
            
        w = j - i
        best_answer = max(best_answer, w)
        
    return best_answer
        
   
nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(search(nums, k))


#--------------------------------------------------
"""def search(nums, k):
    left, i = 0,0 
    zeros = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            zeros += 1
        if zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
    return len(nums)-left

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(search(nums, k))"""