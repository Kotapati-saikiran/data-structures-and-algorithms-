def search(nums,t):
    l = 0
    h = len(nums) - 1
    while l <= h:
        m = l + (h - l) // 2
        if nums[m] == t:
            return m
        elif nums[m] < t:
            l = m + 1
        else:
            h = m - 1
    return -1
nums = [-1,0,3,5,9,12]
t = 9
print(search(nums,t))