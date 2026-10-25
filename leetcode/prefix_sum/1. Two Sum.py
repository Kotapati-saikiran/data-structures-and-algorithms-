def search(nums, target):
    d = {}
    for i in range(len(nums)):
        a = target - nums[i]
        if a in d:
            return [d[a] , i]
        d[nums[i]] = i

nums = [3,2,4]
target = 6
print(search(nums, target))

#----------------------------------
"""def solve(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            a=nums[i]+nums[j]
            if(a==target):
                return [i,j]

nums=list(map(int,input().split()))
target=int(input())
print(solve(nums,target))"""

#---------------------------------------
"""def solve(num,target):
    hashmap={}
    for i in range(len(nums)):
        c=target - nums[i]
        if c in hashmap:
            return [hashmap[c],i]
        hashmap[nums[i]]=i
    return []
nums=list(map(int,input().split()))
target=int(input())
print(solve(nums,target))"""