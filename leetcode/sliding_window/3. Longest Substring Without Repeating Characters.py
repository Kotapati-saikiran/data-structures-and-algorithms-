def search(s):
    n = len(s)
    seen = set()
    l = 0
    r = 0
    max_count = 0
    curr_count = 0
    while r < n:
        while s[r] in seen:
            seen.remove(s[l])
            l += 1
            curr_count -= 1
            
        seen.add(s[r])
        r += 1
        curr_count += 1
        max_count = max(max_count, curr_count)
    return max_count
        

s = "abcabcbb"
print(search(s))