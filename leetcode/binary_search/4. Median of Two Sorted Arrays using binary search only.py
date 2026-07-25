def search(nums1, nums2):
    if nums1 > nums2:
        return search(nums2, nums1)
    m = len(nums1)
    n = len(nums2)
    
    l = 0 
    h = m

    left_side = (m + n + 1) // 2
    
    while l < h:
        mid = (l + h) // 2
        
        partitionA = mid 
        partitionB = left_side - partitionA
        
        LA = 0
        RA = 0
        LB = 0
        RB = 0

        
        if partitionA == 0:
            LA = float('-inf')
        else:
            LA = nums1[partitionA - 1]
            
        if partitionA == m:
            RA = float("inf")
        else:
            RA = nums1[partitionA]
            
        if partitionB == 0:
            LB = float('-inf')
        else:
            LB = nums2[partitionB - 1]
            
        if partitionB == n:
            RB = float("inf")
        else:
            RB = nums2[partitionB]
            
        if LA <= RB and LB <= RA:
            if (m + n) % 2 == 0:
                return (max(LA, LB) + min(RA, RB)) / 2
            else:
                return max(LA, LB)
                
        elif LA > RB:
            h = mid - 1
        else:
            l = mid + 1
        
nums1 = [1,3]
nums2 = [2]
print(search(nums1, nums2))