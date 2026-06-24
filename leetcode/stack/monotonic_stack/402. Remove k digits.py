nums = "9"
k = 1
stack = []
for ch in nums:
    while stack and stack[-1] > ch and k!=0 :
        stack.pop()
        k-=1
    stack.append(ch)
    
while k > 0:
    stack.pop()
    k-=1
res = ''.join(stack)
print(res if res else "0")