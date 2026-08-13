def search(mat):
    r = len(mat) 
    col = len(mat[0]) - 1
    
    l = 0
    h = len(mat[0]) - 1

    while l <= h:
        mid = (l + h) // 2
        m = 0
        maximum_row = 0
        
        for i in range(r):
            if mat[i][mid] > m:
                m = mat[i][mid]
                maximum_row = i
                
        if mid == 0:
            left = -1
        else:
            left = mat[maximum_row][mid - 1]
        if mid == len(mat) - 1:
            right = -1
        else:
            right = mat[maximum_row][mid + 1]
            
                
        if mat[maximum_row][mid] > left and mat[maximum_row][mid] > right:
            return [maximum_row, mid]
            
        elif left > mat[maximum_row][mid]:
            h = mid - 1
        else:
            l = mid + 1
    
mat = [[25,37,23,37,19],[45,19,2,43,26],[18,1,37,44,50]]
print(search(mat))