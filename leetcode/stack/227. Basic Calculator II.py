#Using stack to evaluate the expression
s = "3+2*5/2*4+3"
stack = []
num = 0
sign = "+"

for i, ch in enumerate(s):

    if ch.isdigit():
        num = num * 10 + int(ch)

    if (not ch.isdigit() and ch != " ") or i == len(s) - 1:

        if sign == "+":
            stack.append(num)

        elif sign == "-":
            stack.append(-num)

        elif sign == "*":
            stack.append(stack.pop() * num)

        elif sign == "/":
            stack.append(int(stack.pop() / num))

        sign = ch
        num = 0

print(sum(stack))

#Without using stack to evaluate the expression
"""s = "3+2*5/2*4+3"

num = 0
term = 0
result = 0
sign = "+"

for i, ch in enumerate(s):

    if ch.isdigit():
        num = num * 10 + int(ch)

    if (not ch.isdigit() and ch != " ") or i == len(s) - 1:

        if sign == "+":
            result += term    
            term = num         

        elif sign == "-":
            result += term
            term = -num       

        elif sign == "*":
            term = term * num

        elif sign == "/":
            term = int(term / num)

        sign = ch
        num = 0

result += term
print(result)"""