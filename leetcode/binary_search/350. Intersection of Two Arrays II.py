def intersect(nums1, nums2):
    nums1.sort()
    nums2.sort()
    
    i, j = 0, 0
    result = []
    
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
        else:
            result.append(nums1[i])
            i += 1
            j += 1
            
    return result

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersect(nums1, nums2))

#---------------------------------------------------(using dict)
"""def search(nums1, nums2):
    d = {}
    for i in nums1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    ans = []
    for i in nums2:
        if i in d:
            if d[i] > 0: 
                ans.append(i)
                d[i] -= 1
    return ans
            
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(search(nums1, nums2))"""