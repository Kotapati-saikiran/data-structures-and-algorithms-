def search(s, k):
    
    n = len(s)
    left = 0
    right = 0
    max_freq = 0
    frequencies = {}
    result = 0
    while right < n:
        if s[right] in frequencies:
            frequencies[s[right]] += 1
        else:
            frequencies[s[right]] = 1
        max_freq = max(max_freq, frequencies[s[right]])
        while (right - left + 1) - max_freq > k:
            frequencies[s[left]] -= 1
            left += 1
        result = max(result, (right - left + 1))
        right += 1
    return result  
    
s = "AABABBA"
k = 1
print(search(s, k))

#-------------------------------------------(counts concept)
"""def search(s, k):
    n = len(s)
    if n <= k: return n
    a = s.encode()
    counts = [0] * 91
    maxfreq = l = 0
    cap = 0                      
    w = 0
    for c in a:
        counts[c] += 1
        #v = counts[c]
        if counts[c] > maxfreq:
            maxfreq = counts[c]
            cap = maxfreq + k        
            if cap >= n: return n
        if w < cap:              
            w += 1
        else:
            counts[a[l]] -= 1; l += 1
    return w

s = "AABABBA"
k = 1
print(search(s, k))"""