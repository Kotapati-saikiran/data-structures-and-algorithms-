from collections import deque
def search(nums, limit):
    left, right = 0, 0
    max_dq = deque()
    min_dq = deque()
    best_answer = 0
    for right in range(len(nums)):
        #For max_deque
        while max_dq and nums[max_dq[-1]] <= nums[right]:
            max_dq.pop()
        max_dq.append(right)
        #For min_deque
        while min_dq and nums[min_dq[-1]] >= nums[right]:
            min_dq.pop()
        min_dq.append(right)
        while nums[max_dq[0]] - nums[min_dq[0]] > limit:
            if max_dq and max_dq[0] == left:
                max_dq.popleft()
            if min_dq and min_dq[0] == left:
                min_dq.popleft()
            left += 1
        best_answer = max(best_answer, right - left + 1)
    return best_answer
nums = [8,2,4,7]
limit = 4
print(search(nums, limit))

#------------------------------------------------------------(simple)
"""from collections import deque
def search(nums, limit):
    q , p= deque() , deque()
    l = 0
    for m in nums:
        while q and m > q[-1] : q.pop()
        while p and m < p[-1] : p.pop()
        q.append(m)
        p.append(m)
        if q[0] - p[0] > limit:
            if q[0] == nums[l] : q.popleft()
            if p[0] == nums[l] : p.popleft()
            l +=1 
    return len(nums) - l
nums = [8,2,4,7]
limit = 4
print(search(nums, limit))"""