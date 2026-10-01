def containsNearbyDuplicate(nums, k):
    seen = set()
    left = 0

    for right in range(len(nums)):
        if right - left > k:
            seen.remove(nums[left])
            left += 1
        if nums[right] in seen:
            return True
        seen.add(nums[right])
    return False

nums = [1,2,3,1]
k = 3
print(containsNearbyDuplicate(nums, k))