def search(nums):
    prev_max = nums[0]
    prev_min = nums[0]
    new_max = 0
    new_min = 0
    best_answer = nums[0]
    for i in range(1, len(nums)):
        new_max = max(nums[i] , nums[i] * prev_max, nums[i] * prev_min)
        new_min = min(nums[i] , nums[i] * prev_max, nums[i] * prev_min)
        prev_max = new_max
        prev_min = new_min
        best_answer = max(new_max, new_min, best_answer)
    return best_answer
nums = [2,3,-2,4]
print(search(nums))

#-----------------------------------------------
#Lesson : Maintain multiple states because one state alone may not contain enough information to make the next decision.