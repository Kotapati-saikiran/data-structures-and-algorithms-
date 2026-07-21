def search(nums):
    l = 0
    h = len(nums) - 1
    while l < h:
        mid = (l + h) // 2
        if nums[mid] < nums[mid + 1]:
            l = mid + 1
        elif nums[mid] > nums[mid + 1]:
            h = mid 
    return h
        
nums = [1,2,1,3,5,6,4]
print(search(nums))