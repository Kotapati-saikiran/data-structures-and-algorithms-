def search(nums, target):
    l = 0
    h = len(nums) - 1
    while l <= h:
        mid = (l + h) // 2
        if nums[mid] == target:
            return mid
        if nums[l] <= nums[mid]:
            if nums[l] <= target and target <= nums[mid]:
                h = mid - 1
            else:
                l = mid + 1
        else:
            if nums[mid] <= target and target <= nums[h]:
                l = m + 1
            else:
                h = m - 1
    return -1
nums = [4,5,6,7,0,1,2]
target = 0
print(search(nums, target))