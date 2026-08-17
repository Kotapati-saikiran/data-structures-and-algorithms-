import heapq
def kthSmallest(matrix, k):
    n = len(matrix)
    m = len(matrix[0])

    pq = []

    for r in range(min(n, k)):
        heapq.heappush(pq, (matrix[r][0], r, 0))

    for _ in range(1, k):
        val, r, c = heapq.heappop(pq)

        if c + 1 < m:
            heapq.heappush(pq, (matrix[r][c + 1], r, c + 1))

    return pq[0][0]
    
matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
print(kthSmallest(matrix, k))