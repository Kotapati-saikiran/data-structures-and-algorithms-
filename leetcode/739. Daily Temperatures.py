tps = [73,74,75,71,69,72,76,73]
n = len(tps)
stack = []
ans = [0] * n
for i in range(n):
    while(stack and tps[i] > tps[stack[-1]]):
        x = i - stack[-1]
        ans[stack[-1]] = x
        stack.pop()
    stack.append(i)
print(ans)