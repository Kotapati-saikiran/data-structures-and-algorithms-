def search(nums):
    l = 1
    h = nums // 2
    ans = 0
    
    while l <= h:
        mid = (l + h) // 2
        s = mid * mid
        if s == nums:
            return mid
        if s < nums:
            ans = mid
            l = mid + 1
        else:
            h = mid - 1
    return ans
nums = 8
print(search(nums))