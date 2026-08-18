def countOfSmallerOrEqualElements(matrix, val):
    n = len(matrix)
    m = len(matrix[0])
    count = 0

    for i in range(n):
        # C++ upper_bound equivalent
        l = 0
        r = m

        while l < r:
            mid = (l + r) // 2

            if matrix[i][mid] <= val:
                l = mid + 1
            else:
                r = mid

        count += l

    return count


def kthSmallest(matrix, k):
    n = len(matrix)
    m = len(matrix[0])
    
    #range for the binary search
    l = matrix[0][0]
    r = matrix[n - 1][m - 1]
    ans = -1
    while l <= r:
        mid = l + (r - l) // 2
        count = countOfSmallerOrEqualElements(matrix, mid)

        if count >= k:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1

    return ans
    
matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
print(kthSmallest(matrix, k))