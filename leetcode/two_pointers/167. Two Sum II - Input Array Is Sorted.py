def search(nums, target):
    l = 0
    h = len(nums) - 1
    while l < h:
        x = nums[l] + nums[h]
        if x == target:
            return [l + 1, h + 1]
        elif x < target:
            l = l + 1
        else:
            h = h - 1
            
nums = [2,7,11,15]
target = 9
print(search(nums, target))