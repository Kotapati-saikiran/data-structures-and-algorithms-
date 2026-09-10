def search(nums, target):
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n - 1):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n -1):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            k = j + 1
            l = n - 1
            while k < l:
                quad_sum = nums[i] + nums[j] + nums[k] + nums[l]
                if quad_sum < target:
                    k += 1
                elif quad_sum > target:
                    l -= 1
                elif quad_sum == target:
                    res.append([nums[i], nums[j], nums[k], nums[l]])
                    k += 1
                    l -= 1
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1
    return res
                
nums = [1,0,-1,0,-2,2]
target = 0
print(search(nums, target))