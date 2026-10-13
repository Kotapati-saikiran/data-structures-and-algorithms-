def search(target, nums):
    n = len(nums)
    left = 0
    right = 0
    array = 0
    best_answer = float('inf')

    while right < n or array >= target:
        if array < target:
            array += nums[right]
            right += 1
        else:
            best_answer = min(best_answer, right - left)
            array -= nums[left]
            left += 1

    return 0 if best_answer == float('inf') else best_answer


target = 7
nums = [2, 3, 1, 2, 4, 3]
print(search(target, nums))