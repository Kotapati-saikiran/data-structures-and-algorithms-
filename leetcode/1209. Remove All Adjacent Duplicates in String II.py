s = "deeedbbcccbdaa"
stack = []
k = 3
for char in s:
    if stack and stack[-1][0] == char:
        stack[-1][1]+=1
        if stack[-1][-1] == k:
            stack.pop()
    else:
        stack.append([char,1])

res = ""
for ch in stack:
    x = ch[0][0] * ch[-1]
    res+= x
print(res)