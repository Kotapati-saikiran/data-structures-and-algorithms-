def search(nums):
    l = 0
    h = len(nums) - 1
    while l < h:
        mid = (l + h) // 2
        if nums[l] == nums[mid] == nums[h]:
            l += 1
            h -= 1
        elif nums[mid] > nums[h]:
            l = mid + 1
        elif nums[mid] <= nums[h]:
            h = mid 
    return nums[h]

nums = [1,1,1,1,0,1]
print(search(nums))