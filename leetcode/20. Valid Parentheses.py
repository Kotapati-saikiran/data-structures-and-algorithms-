s = "()"
stack = []
for char in s:
    if char in "([{":
        stack.append(char)
    elif char == ")":
        if not stack or stack[-1] != "(":
            print(False)
            break
        stack.pop()
    elif char == "]":
        if not stack or stack[-1] != "[":
            print(False)
            break
        stack.pop()
    elif char == "}":
        if not stack or stack[-1] != "{":
            print(False)
            break
        stack.pop()
else:
    print(len(stack) == 0)

#----------------------------------------------------------(8 ms)
"""s="{}"
stack = []
for c in s:
    if c in "({[":
        stack.append(c)
    elif c in ")}]":
        if not stack:
            print(False)
        top = stack.pop()
        if ((c == ')' and top != '(') or (c == '}' and top != '{') or (c == ']' and top != '[')):
            print(False)
if not stack:
    print(True)
else:
    print(False)"""