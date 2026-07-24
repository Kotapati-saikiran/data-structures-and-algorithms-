def search(nums, target):
    n = len(nums)
    prefix_sums = [0] * (n + 1) # prefix sums of sorted array then we will perform bs
    prefix_sums[0] = 0
    
    for i in range(1,len(prefix_sums)):
        prefix_sums[i] += prefix_sums[i - 1] + nums[i - 1]
        
    length = float('inf')
    for j in range(len(prefix_sums) - 1, -1 , -1):
        x = prefix_sums[j] - target
        
        l = 0
        r = j - 1
        ans = -1
        while l < r:
            mid = (l + r) // 2
            if prefix_sums[mid] <= x:
                ans = mid
                l = mid + 1
            else:
                mid -= 1
                r = mid - 1
        if ans != -1:
            length = min(length, j - mid)
    if length == float('inf'):
        return 0
    return length
                
nums = [2,3,1,2,4,3]
target = 7
print(search(nums, target))

#main formula of the problem
"""prefix[left] <= current - target
current - prefix[left] >= target"""