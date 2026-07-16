import math
def search(piles, h):
    l = 1
    r = max(piles)
    best_answer = float('inf')
    while l <= r:
        k = (l + r) // 2
        sum = 0
        for p in piles:
            sum += math.ceil(p/k)
        if sum <= h:
            r = k - 1
            best_answer = min(best_answer, k)
        else:
            l = k + 1
        sum = 0
    return best_answer
piles = [3,6,7,11]
h = 8
print(search(piles, h))

#-----------------------------------------(advanced only mathematical thinking no lib's)
"""def search(piles, h):
    lo = sum(piles)
    hi = -(lo // (len(piles) - h - 1))
    lo = (lo - 1) // h + 1
    while lo < hi:
        mid = (lo + hi) >> 1
        score = -sum(-pile // mid for pile in piles)
        if h < score:
            lo = mid + 1
        else:
            hi = mid
    return lo
piles = [3,6,7,11]
h = 8
print(search(piles, h))"""