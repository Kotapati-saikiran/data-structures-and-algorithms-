s = "(1+(4+5+2)-3)+(6+8)"
num = 0
sign = "+"
result = 0
stack = []
for ch in s:
    if ch.isdigit():
        num = num * 10 + int(ch)
    elif ch == "+":
        if sign == "+":
            result += num
        else:
            result -= num
        num = 0
        sign = "+"
    elif ch == "-":
        if sign == "+":
            result += num
        else:
            result -= num
        num = 0
        sign = "-"
    elif ch == "(":
        stack.append((result, sign))
        result = 0
        sign = "+"
        num = 0
    elif ch == ")":
        if sign == "+":
            result += num
        else:
            result -= num
        prev_res, prev_sign = stack.pop()
        if prev_sign == "+":
            result = prev_res + result
        else:
            result = prev_res - result
        num = 0
if sign == "+":
    result += num
else:
    result -= num
print(result)

"""Pattern: Expression Parsing + Context Management
Core Observation: Process a number as soon as it is finished. Parentheses don't perform arithmetic—they create and close calculation contexts.
Reusable Idea: Separate variable responsibilities (num, result, sign, stack). Save context before entering nested work and restore it when that work finishes."""