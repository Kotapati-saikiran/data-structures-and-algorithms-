def check(nums):
    count = 0
    n = len(nums)
    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            count += 1
    return count <= 1
    
nums=[2,1,3,4]
res=check(nums)
print(res)