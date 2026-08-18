import heapq
def kthSmallestPrimeFraction(arr, k):
    n = len(arr)
    pq = []

    # Push fractions: arr[i] / arr[n-1]
    for i in range(min(n - 1, k)):
        heapq.heappush(pq, (arr[i] / arr[-1], i, n - 1))

    # Find the kth smallest fraction
    for _ in range(1, k):
        _, i, j = heapq.heappop(pq)

        if j - 1 > i:
            heapq.heappush(pq,(arr[i] / arr[j - 1], i, j - 1))
    _, i, j = pq[0]
    return [arr[i], arr[j]]
    
arr = [1,2,3,5]
k = 3
print(kthSmallestPrimeFraction(arr, k))