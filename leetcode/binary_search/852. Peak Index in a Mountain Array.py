def search(nums):
    l = 0
    r = len(nums) - 1
    while l < r:
        m = l + (r - l) // 2
        if nums[m] < nums[m + 1]:
            l = m + 1
        else: 
            r = m
    return r
nums = [0,2,5,8,7,4,1]
print(search(nums))