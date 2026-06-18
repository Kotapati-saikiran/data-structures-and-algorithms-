s = "100[leetcode]"
stack = []
cur_num = 0
cur_str = ""
for char in s:
    if char.isdigit():
        cur_num = cur_num * 10 + int(char)
    elif char == "[":
        stack.append((cur_str, cur_num))
        cur_num = 0
        cur_str = ""
    elif char.isalpha():
        cur_str+=char
    elif char == "]":
        x = stack[-1][0] + cur_str * stack[-1][-1]
        stack.pop()
        cur_str = x
        
print(cur_str)