logs = ["./","../","./"]
stack = []
for char in logs:
    if char == "../":
        if stack:
            stack.pop()
    elif char == "./":
        pass
    else:
        stack.append(char)
print(len(stack))