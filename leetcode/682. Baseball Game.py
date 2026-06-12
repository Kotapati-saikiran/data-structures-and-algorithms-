ops = ["5","-2","4","C","D","9","+","+"]
n = len(ops)
stack = []
for i in range(n):
    if(ops[i] == "C"):
        stack.pop()
    elif(ops[i] == "D"):
        x = 2 * int(stack[-1])
        stack.append(str(x))
    elif(ops[i] == "+"):
        y = int(stack[-2]) + int(stack[-1])
        stack.append(str(y))
    else:
        stack.append(ops[i])
        
a = list(map(int, stack))
print(sum(a))