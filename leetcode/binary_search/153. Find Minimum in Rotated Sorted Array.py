def search(nums):
    l = 0
    h = len(nums) - 1
    while l < h:
        mid = (l + h) // 2
        if nums[mid] > nums[h]:
            l = mid + 1
        elif nums[mid] < nums[h]:
            h = mid
    return nums[l]
        
nums = [3,4,5,1,2]
print(search(nums))