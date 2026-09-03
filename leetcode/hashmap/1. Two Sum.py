def search(nums, target):
    d = {}
    for i in range(len(nums)):
        a = target - nums[i]
        if a in d:
            return [d[a] , i]
        d[nums[i]] = i

nums = [3,2,4]
target = 6
print(search(nums, target))