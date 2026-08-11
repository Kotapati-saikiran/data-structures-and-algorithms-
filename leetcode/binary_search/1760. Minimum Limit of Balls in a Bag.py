import math
def search(nums, maxOperations):
    l = 1
    h = max(nums)
    best_answer = 0
    while l <= h:
        mid = (l + h) // 2
        ans = 0
        for i in nums:
            ans += math.ceil(i/mid) - 1
            
        if ans <= maxOperations:
            best_answer = mid
            h = mid - 1
        else:
            l = mid + 1
    return best_answer
            
nums = [2,4,8,2]
maxOperations = 4
print(search(nums, maxOperations))