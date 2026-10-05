def search(nums):
    l = 0 
    r = 0
    count = 0
    best_answer = 0

    while r < len(nums):
        if nums[l] == 1 and nums[r] == 1:
            count += 1
            best_answer = max(best_answer, count)
            r += 1
        else:
            count = 0
            l = r + 1
            r += 1
    return best_answer
    
nums = [1,0,1,1,0,1]
print(search(nums))