def search(nums, target):
    n = len(nums)
    i = 0 
    j = n - 1
    while i < n:
        while j >= 0:
            if i == j:
                break
            elif (nums[i] + nums[j]) == target:
                return [i, j]
                break
            else:
                j -= 1
        j = n - 1
        i += 1

nums = [3,2,4]
target = 6
print(search(nums, target))