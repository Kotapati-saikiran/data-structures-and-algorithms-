def search(m, n, k):
    l = 1
    h = m * n
    best_answer = 0
    while l <= h:
        mid = l + (h - l) // 2
        i = 1
        count = 0
        while i <= m:
            count += min(n, mid//i)
            i += 1
        if count < k:
            l = mid + 1
        elif count >= k:
            best_answer = mid
            h = mid - 1
    return best_answer
            
m = 3
n = 3
k = 5
print(search(m, n, k))