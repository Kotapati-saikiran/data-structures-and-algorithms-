asteroids = [3,5,-6,2,-1,4]
stack = []
for num in asteroids:
    alive = True
    while alive and stack and stack[-1] > 0 and num < 0:
        if abs(num) > abs(stack[-1]):
            stack.pop()
        elif abs(num) < abs(stack[-1]):
            alive = False
        elif abs(num) == abs(stack[-1]):
            stack.pop()
            alive=False
    if alive:
        stack.append(num)
print(stack)

#--------------------------------------
"""asteroids = [3, 5, -6, 2, -1, 4]
st = []
for a in asteroids:
    while st and a < 0 and st[-1] > 0:
        if st[-1] < -a:
            st.pop()
            continue
        elif st[-1] == -a:
            st.pop()
        break
    else:
        st.append(a)
print(st) """