heights = [2,1,5,6,2,3]
n = len(heights)
left = [-1] * n
right =[n] * n
stack = []

for i in range(n): #left to right
    while stack and heights[stack[-1]] >= heights[i]:
        stack.pop()
    if stack:
        left[i] = stack[-1]
    else:
        left[i] = -1
    stack.append(i)
stack.clear()

for i in range(n-1,-1,-1): # right to left 
    while stack and heights[stack[-1]] >= heights[i]:
        stack.pop()
    if stack:
        right[i] = stack[-1]
    else:
        right[i] = n
    stack.append(i)

max_area = 0
for i in range(n):
    width = right[i] - left[i] - 1
    max_area = max(max_area, heights[i] * width)

print(max_area)