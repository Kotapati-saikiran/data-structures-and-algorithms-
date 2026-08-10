def search(nums, k):
    l = max(nums)
    h = sum(nums)
    best_answer = 0
    while l <= h:
        mid = (l + h) // 2
        curr = 0
        subarr = 1
        for i in nums:
            if curr + i <= mid:
                curr += i
            else:
                subarr += 1
                curr = i
        if subarr <= k:
            best_answer = mid
            h = mid - 1
        else:
            l = mid + 1
    return best_answer
            
        
nums = [7,2,5,10,8]
k = 2
print(search(nums, k))