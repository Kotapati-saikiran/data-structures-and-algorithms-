import math
def search(nums, threshold):
    l = 1
    h = max(nums)
    val = 0
    while l <= h:
        mid = (l + h) // 2
        ans = 0
        for i in nums:
            x = math.ceil(i/mid)
            ans += x
        if ans <= threshold:
            val = mid
            h = mid - 1
            continue
        else:
            l = mid + 1
    return val
        
nums = [21212,10101,12121]
threshold = 1000000
print(search(nums, threshold))