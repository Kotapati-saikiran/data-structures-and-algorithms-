def search(nums,t):
    l = 0
    h = len(nums) - 1
    ans = nums[0]
    
    while l <= h:
        m = l + (h - l) // 2
        if nums[m] > t:
            ans = nums[m]
            h = m - 1
        else:
            l = m + 1
    return ans
    
nums = ["c","f","j"]
t = "c"
print(search(nums,t))