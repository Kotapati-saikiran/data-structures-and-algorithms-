def search(bloomDay, m, k):
    l = min(bloomDay)
    h = max(bloomDay)
    best_answer = -1
    
    while l <= h:
        mid = (l + h) // 2
        c = 0
        b = 0
        for i in bloomDay:
            if i <= mid:
                c+=1
                if c == k:
                    c = 0
                    b += 1
            else:
                c = 0
                
        if b >= m:
            best_answer = b
            h = mid - 1
        else:
            l = mid + 1
            
    return  best_answer



bloomDay = [1,10,3,10,2]
m = 3
k = 1
print(search(bloomDay, m, k))