def search(nums, k):
    if k == 0:
        return 0
        
    n = len(nums)
    left = 0
    product = 1
    count = 0 
    for right in range(n):
        product *= nums[right]
        while product >= k:
            product //= nums[left]
            left += 1
        count += right - left + 1
    return count
            
nums = [10,5,2,6]
k = 100
print(search(nums, k))