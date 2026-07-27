def search(nums1, nums2):
    nums1.sort()
    ans = set()
    
    for num in nums2:
        l = 0
        r = len(nums1) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if nums1[mid] == num:
                ans.add(num)
                break
            elif nums1[mid] < num:
                l = mid + 1
            else:
                r = mid - 1
    return list(ans)

nums1 = [1,2,2,1]
nums2 = [2,2]
print(search(nums1, nums2))


#------------------------------------(Using Hash Table)
"""def search(nums1, nums2):
    d = {}
    for i in nums1:
        if i not in d:
            d[i] = 1
    for i in nums2:
        if i in d and d[i] == 1:
            d[i] == 2
    res = []

    for i in d:
        if d[i] == 2:
            res.append(i)
    return res
nums1 = [1,2,2,1]
nums2 = [2,2]
print(search(nums1, nums2))
"""

#------------------------------------------(Using set)
"""def search(nums1, nums2):
    seen = set(nums1)
    ans = set()

    for num in nums2:
        if num in seen:
            ans.add(num)

    return list(ans)
nums1 = [1,2,2,1]
nums2 = [2,2]
print(search(nums1, nums2))"""