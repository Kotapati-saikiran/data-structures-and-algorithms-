def search(time, totalTrips):
    l = 1
    h = min(time) * totalTrips
    best_answer = float('inf')
    while l <= h:
        mid = (l + h) // 2
        ans = 0
        for i in time:
            ans += mid // i
        if ans >= totalTrips:
            best_answer = mid
            h = mid - 1
        else:
            l = mid + 1
    return best_answer
             
time = [1,2,3]
totalTrips = 5
print(search(time, totalTrips))