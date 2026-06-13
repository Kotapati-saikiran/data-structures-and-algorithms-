tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
stack = []
for token in tokens:
    if token == "+":
        b = stack.pop()
        a = stack.pop()
        stack.append(a + b)
    elif token == "-":
        b = stack.pop()
        a = stack.pop()
        stack.append(a - b)
    elif token == "*":
        b = stack.pop()
        a = stack.pop()
        stack.append(a * b)
    elif token == "/":
        b = stack.pop()
        a = stack.pop()
        stack.append(int(a / b)) 
    else:
        stack.append(int(token))
print(stack[-1])

#----------------------------------------------------------
"""tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
stack = []
for t in tokens:
    if t in ['+', '-', '*', '/']:
        num1 = stack.pop()
        num2 = stack.pop()
        if t == '+':
            stack.append(num2 + num1)
        elif t == '-':
            stack.append(num2 - num1)
        elif t == '*':
            stack.append(num2 * num1)
        elif t == '/':
            stack.append(int(float(num2) / num1))
    else:
        stack.append(int(t))
print(stack[-1])"""