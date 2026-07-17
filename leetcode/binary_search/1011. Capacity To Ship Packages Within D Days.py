def search(weights, days):
    
    l = max(weights)
    r = sum(weights)
    best_answer = float('inf')
    while l <= r:
        mid = (l + r) // 2
        
        capacity = 0
        count_of_days = 1
        
        for w in weights:
            capacity += w
            
            if capacity <= mid:
                continue
            else:
                capacity = 0
                capacity += w
                count_of_days += 1
                
        if count_of_days <= days:
            best_answer = min(best_answer, mid)
            r = mid - 1
        else:
            l = mid + 1
    return best_answer
                 
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5    
print(search(weights, days))