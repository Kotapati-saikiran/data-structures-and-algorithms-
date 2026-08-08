def search(position, m):
    position.sort()
    n = len(position)
    
    l = 1
    h = position[-1] - position[0]
    res = 0
    
    while l <= h:
        mid = (l + h) // 2
        balls = 1
        pos = position[0]
        for i in range(1, len(position)):
            if position[i] - pos >= mid:
                balls += 1
                pos = position[i]
        if balls >= m:
            res = mid
            l = mid + 1
        else:
            h = mid - 1
    return res
        
position = [1,2,3,4,7]
m = 3    
print(search(position, m))