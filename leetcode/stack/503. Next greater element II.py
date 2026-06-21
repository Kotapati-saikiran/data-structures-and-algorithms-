nums = [1,2,1]
a = nums + nums
n= len(a)
stack = []
ans = [-1] * len(nums)
for i in range(n):
    while stack and a[i] > a[stack[-1]]:
        ans[stack[-1]%len(nums)] = a[i]
        stack.pop()
    stack.append(i)
    
for i in range(n): #second pass not written also no problem helpful in many problems.
    while stack and a[i] > a[stack[-1]]:
        ans[stack[-1]%len(nums)] = a[i]
        stack.pop()
print(ans)