def search(matrix, target):
    r = len(matrix)
    c = len(matrix[0])
    
    l = 0
    h = r * c - 1
    
    while l <= h:
        mid = (l + h) // 2
        row = mid // c
        col = mid % c
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] <= target:
            l = mid + 1
        else:
            h = mid - 1
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(search(matrix, target))