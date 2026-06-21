path = "/home/user/Documents/../Pictures"
a = path.split("/")
stack = []

for char in a:
    if char == '':
        pass
    elif char == '.':
        pass
    elif char == '..':
        if stack:
            stack.pop()
    else:
        stack.append(char)

if not stack:
    print("/")
else:
    s = "/"
    for i in range(len(stack)):
        s += stack[i]
        if i != len(stack) - 1:
            s += "/"
    print(s)