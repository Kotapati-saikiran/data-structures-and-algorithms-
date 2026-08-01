def search(aliceSizes, bobSizes):
    aliceSizes.sort()
    
    sumA = sum(aliceSizes)
    sumB = sum(bobSizes)
    
    diff = (sumA - sumB) // 2
    
    for j in bobSizes:
        target = j + diff
        
        l = 0 
        h = len(aliceSizes) - 1
        while l <= h:
            mid = (l + h) // 2
            if aliceSizes[mid] == target:
                return [aliceSizes[mid], j]
            elif aliceSizes[mid] < target:
                l = mid + 1
            else:
                h = mid - 1

aliceSizes = [1,2]
bobSizes = [2,3]
print(search(aliceSizes, bobSizes))

#---------------------------------------------------(Using Hash Tabel)
"""def search(aliceSizes, bobSizes):
    alice_set = set(aliceSizes)
    
    sumA = sum(aliceSizes)
    sumB = sum(bobSizes)
    
    diff = (sumA - sumB) // 2
    
    for j in bobSizes:
        target = j + diff
        if target in alice_set:
            return [target, j]

aliceSizes = [1,2]
bobSizes = [2,3]
print(search(aliceSizes, bobSizes))"""

#-------------------------------------------
"""def search(aliceSizes, bobSizes):
    aliceSizes.sort()
    sumA = sum(aliceSizes)
    sumB = sum(bobSizes)
    diff = (sumA - sumB) // 2
    ans = []
    for j in bobSizes:
        target = j + diff
        if target in aliceSizes:
            ans.append(target)
            ans.append(j)
            break
    return ans

aliceSizes = [1,1]
bobSizes = [2,2]
print(search(aliceSizes, bobSizes))"""