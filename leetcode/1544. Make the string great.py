s = "leEeetcode"
stack = []
for char in s:
    if stack and abs(ord(stack[-1]) - ord(char)) == 32:
        stack.pop()
    else:
        stack.append(char)
print("".join(stack))

#---------------------------------------------------------------------(0ms)
"""s = "leEeetcode"
alpc=[]
arr=[]
for i in range(0,26):
    alpc.append(chr(ord('A')+i))
for i in s:
    if arr and i.swapcase() == arr[-1]: # swapcase changes E to e -> upper to lower and lower to upper 
        arr.pop() 
    else:
        arr.append(i)
print("".join(arr))"""