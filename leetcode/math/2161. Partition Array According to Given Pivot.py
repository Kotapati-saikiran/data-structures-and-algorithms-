nums = [9,12,5,10,14,3,10]
pivot = 10
a = len(nums)
left = []
mid= []
right = []
for i in range(a):
    if(nums[i] < pivot):
        left.append(nums[i])
    elif(nums[i] == pivot):
        mid.append(nums[i])
    else:
        right.append(nums[i])
y = left + mid + right
print(y)

#----------------------------------------------(Two pointer approach)
"""nums = [9,12,5,10,14,3,10]
n = len(nums)
ans = [0] * n

left = 0
right = n - 1

i = 0
j = n - 1

while i < n:
    if nums[i] < pivot:
        ans[left] = nums[i]
        left += 1
    if nums[j] > pivot:
        ans[right] = nums[j]
        right -= 1
    i += 1
    j -= 1

while left <= right:
    ans[left] = pivot
    left += 1
print(ans)"""