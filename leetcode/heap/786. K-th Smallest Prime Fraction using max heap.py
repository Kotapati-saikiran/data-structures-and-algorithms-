import heapq
def kthSmallestPrimeFraction(arr, k):
    n = len(arr)
    pq = []

    for i in range(n):
        for j in range(i + 1, n):
            val = arr[i] / arr[j]
            heapq.heappush(pq, (-val, i, j))

            if len(pq) > k:
                heapq.heappop(pq)

    _, i, j = pq[0]
    return [arr[i], arr[j]]
arr = [1,2,3,5]
k = 3
print(kthSmallestPrimeFraction(arr, k))