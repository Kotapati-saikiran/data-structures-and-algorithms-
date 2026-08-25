def search(nums):
    n = len(nums)
    i = 0
    j = 0
    while j < n:
        if nums[j] != 0:
            nums[j] , nums[i] = nums[i], nums[j]
            j += 1
            i += 1
        else:
            j += 1
    return nums
nums = [0,1,0,3,12]
print(search(nums))