def search(nums, target):
    n = len(nums)
    nums.sort()
    best_answer = nums[0] + nums[1] + nums[2]
    for i in range(n - 1):
        j = i + 1
        k = n - 1
        while j < k:
            current_sum = nums[i] + nums[j] + nums[k]
            distance = abs(current_sum - target)
            best_distance = abs(best_answer - target)
            
            if current_sum == target:
                return current_sum
            if distance < best_distance:
                best_answer = current_sum
            if current_sum < target:
                j += 1
            else:
                k -= 1
    return best_answer
             
nums = [-1,2,1,-4]
target = 1
print(search(nums, target))