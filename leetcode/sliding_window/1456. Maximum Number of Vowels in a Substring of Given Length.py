def search(s, k):
    n = len(s)
    l = 0
    r = k - 1
    vowel_count = 0
    best_answer = 0
    vowels = "aeiou"
    
    for char in s[l : r + 1]:
        if char in vowels:
            vowel_count += 1
        best_answer = vowel_count
            
    while r < n - 1:
        if s[l] in vowels:
            vowel_count -= 1
        r += 1
        if s[r] in vowels:
            vowel_count += 1
        l += 1
        best_answer = max(best_answer, vowel_count)
        
    return best_answer
    
s = "abciiidef"
k = 3
print(search(s, k))