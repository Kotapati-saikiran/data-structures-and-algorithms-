target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

cars = sorted(zip(position, speed))

stack = []

for pos, spd in reversed(cars):

    time = float(target - pos) / spd

    if not stack or time > stack[-1]:
        stack.append(time)

print(len(stack))
stack

#-----------------------------------------------------
"""target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
map = {}
        
for i in range(len(speed)):
    map[position[i]]=speed[i]

s=sorted(map.keys(),reverse=True)

fleet = 0
prev = 0

for x in s:
    
    time = float(target - x) / map[x]
    
    if time > prev:
        fleet += 1
        prev = time
fleet"""