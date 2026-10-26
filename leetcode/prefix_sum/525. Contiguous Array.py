def findMaxLength(nums):
    balance = 0
    max_len = 0
    index = {0:-1}
    for i in range(len(nums)):
        if nums[i] == 0:
            balance -= 1
        else:
            balance += 1
        if balance in index:
            max_len = max(max_len, i - index[balance])
        else:
            index[balance] = i
    return max_len
nums = [0,1,1,1,1,1,0,0,0]
print(findMaxLength(nums))