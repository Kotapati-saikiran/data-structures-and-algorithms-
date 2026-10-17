def search(nums):
    n = len(nums)
    s = set()
    left = 0
    right = 0
    curr_sum = 0
    best_answer = 0
    while right < n:
        while nums[right] in s:
            s.remove(nums[left])
            curr_sum -= nums[left]
            left += 1
        s.add(nums[right])
        curr_sum += nums[right]
        right += 1
        best_answer = max(best_answer, curr_sum)
    return best_answer

nums = [4,2,4,5,6]
print(search(nums))