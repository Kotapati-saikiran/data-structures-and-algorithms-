def search(nums):
    res = []
    sum = 0
    for i in range(len(nums)):
        sum += nums[i]
        res.append(sum)
    return res
        
nums = [1,2,3,4]
print(search(nums))