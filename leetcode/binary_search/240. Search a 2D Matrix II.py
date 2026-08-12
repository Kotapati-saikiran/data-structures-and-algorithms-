def search(matrix, target):
    row = 0
    col = len(matrix[0]) - 1
    while row <= len(matrix) - 1 and col >= 0:
        curr = matrix[row][col]
        if curr == target:
            return True
        elif curr < target:
            row += 1
        elif curr > target:
            col -= 1
    return False
    
matrix = [[1,4],[2,5]]
target = 2
print(search(matrix, target))