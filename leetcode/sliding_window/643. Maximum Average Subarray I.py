def search(nums, k):
    l = 0
    r = k
    old_sum = sum(nums[l : r])
    best_answer = old_sum
    while r < len(nums):
        avg_sum = (old_sum - nums[l]) + nums[r]
        best_answer = max(best_answer, avg_sum)
        old_sum = avg_sum
        l += 1
        r += 1
    return best_answer/k


nums = [1,12,-5,-6,50,3]
k = 4
print(search(nums, k))