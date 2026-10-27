def search(nums):
    x = sum(nums)
    y = 0
    for i in range(1,len(nums)):
        y += i
    return y - x
nums = [3,0,1]
print(search(nums))