def search(nums, k):
    n = len(nums)
    nums.sort()
    
    l = 0
    h = max(nums) - min(nums)
    best_answer = 0
    while l <= h:
        mid = (l + h) // 2
        i = 0 
        j = 1
        count = 0
        #Two pointers
        while i < n:
            while j < n and nums[j] - nums[i] <= mid:
                j += 1
            count += j - i - 1
            i += 1
        #Binary search
        if count < k:
            l = mid + 1
        elif count >= k:
            best_answer = mid
            h = mid - 1
    return best_answer
            
 
nums = [1,3,6,7]
k = 3
print(search(nums, k))