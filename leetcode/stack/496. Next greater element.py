nums1 = [4,1,2]
nums2 = [1,3,4,2]
stack = []
for i in range(len(nums1)):
    for j in range(len(nums2)):
        if(nums1[i] == nums2[j]):
            for k in range(j + 1, len(nums2)-1):
                if(nums2[k] > nums2[j]):
                    stack.append(nums2[k])
                    break
            else:
                stack.append(-1)
print(stack)
#----------(Monotic stack - Find the next/previous greater/smaller element efficiently without repeatedly scanning the array.)(2ms)
"""nums1 = [4,1,2]
nums2 = [1,3,4,2]
stack = []
hash_map = {}
for num in nums2:
    while(stack and num > stack[-1]):
        hash_map[stack.pop()] = num
    stack.append(num)
    
while stack:
    hash_map[stack.pop()] = -1
res = []
for num in nums1:
    res.append(hash_map[num])

print(res)"""