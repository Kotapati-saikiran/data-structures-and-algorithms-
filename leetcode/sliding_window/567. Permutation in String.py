def search(s1, s2):
    # hashmap - 1
    map1 = {}
    for ch in s1:
        if ch in map1:
            map1[ch] += 1
        else:
            map1[ch] = 1
    # hashmap - 2
    map2 = {}
    l = 0
    r = len(s1) - 1
    for ch in s2[l : r + 1]:
        if ch in map2:
            map2[ch] += 1
        else:
            map2[ch] = 1
            
    while r < len(s2):
        if map1 == map2:
            return True
            
        left_char = s2[l]
        map2[left_char] -= 1
        
        if map2[left_char] == 0:
            del map2[left_char]
            
        l += 1
        r += 1
        
        if r < len(s2):
            right_char = s2[r]
            
            if right_char in map2:
                map2[right_char] += 1
            else:
                map2[right_char] = 1
    return False
            
            
s1 = "ab"
s2 = "eidbaooo"
print(search(s1, s2))