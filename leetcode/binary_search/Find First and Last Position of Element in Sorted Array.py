def search(nums,t):
    l = 0
    h = len(nums) - 1
    first = -1
    while l <= h:
        m = l + (h - l) // 2
        if nums[m] == t:
            first = m
            h = m - 1
        elif nums[m] < t:
            l = m + 1
        else:
            h = m - 1

    l = 0
    h = len(nums) - 1
    last = -1
    
    while l <= h:
        m = l + (h - l) // 2
        if nums[m] == t:
            last = m
            l = m + 1
        elif nums[m] < t:
            l = m + 1
        else:
            h = m - 1
    return [first, last]
    
nums =  [5,7,7,8,8,10]
t = 8
print(search(nums,t))