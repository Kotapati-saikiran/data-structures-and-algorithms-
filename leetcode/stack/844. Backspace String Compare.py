s = "a##c"
t = "#a#c"

stack1 = []
stack2 = []
for char in s:
    if(len(stack1) == 0 and char == "#"):
        pass
    elif(char == "#"):
        stack1.pop()
    else:
        stack1.append(char)

for char in t:
    if(len(stack2) == 0 and char == "#"):
        pass
    elif(char == "#"):
        stack2.pop()
    else:
        stack2.append(char)

if(stack1 == stack2):
    print(True)
else:
    print(False)