def search(nums, k):
    prefix_sum = 0
    count = 0 
    remainder_frequency = {0:1}
    for i in range(len(nums)):
        prefix_sum += nums[i]
        r = prefix_sum % k
        if r in remainder_frequency:
            count += remainder_frequency[r]
            remainder_frequency[r] += 1
        else:
            remainder_frequency[r] = 1
    return count

nums = [4,5,0,-2,-3,1]
k = 5
print(search(nums, k))