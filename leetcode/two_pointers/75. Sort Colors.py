def search(nums):
    red = 0
    blue = len(nums) - 1
    i = 0
    while i <= blue:
        if nums[i] == 0: # red
            nums[i], nums[red] = nums[red], nums[i]
            if i == red:
                i += 1
            red += 1
        elif nums[i] == 2: # blue
            nums[i], nums[blue] = nums[blue], nums[i]
            blue -= 1
        else:
            i += 1
    return nums
nums = [2,0,1]
print(search(nums))