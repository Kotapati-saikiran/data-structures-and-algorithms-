def search(nums, target):
    l = 0
    h = len(nums) - 1
    while l <= h:
        mid = (l + h) // 2
        if nums[mid] == target:
            return True
        if nums[l] == nums[mid]:
            l += 1
            continue
        if nums[l] <= nums[mid]:
            if nums[l] <= target and target <= nums[mid]:
                h = mid - 1
            else:
                l = mid + 1
        else:
            if nums[mid] <= target and target <= nums[h]:
                l = mid + 1
            else:
                h = mid - 1
    return False
nums = [1,0,1,1,1]
target = 0
print(search(nums, target))