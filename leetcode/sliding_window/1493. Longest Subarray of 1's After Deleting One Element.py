def search(nums):
    n = len(nums)
    left = 0 
    right = 0 
    zero_counter = 0
    w = 0
    best_answer = 0
    while right < n:
        if nums[right] == 0:
            zero_counter += 1
        while zero_counter > 1:
            if nums[left] == 0:
                zero_counter -= 1
            left += 1
        w = right - left
        best_answer = max(best_answer, w)
        right += 1
    return best_answer
                
nums = [0,1,1,1,0,1,1,0,1]
print(search(nums))

#-----------------------------------------------------
"""from itertools import groupby
from itertools import pairwise

def search(nums):
    if 1 not in nums: return 0
    if 0 not in nums: return len(nums)-1

    arr = [list(g) for k, g in groupby(nums)]
    arr = [sum(x) for x in arr if x!= [0]]
    if len(arr) == 1: return arr[0]
    return max(map(sum,pairwise(arr)))
                
nums = [0,1,1,1,0,1,1,0,1]
print(search(nums))"""