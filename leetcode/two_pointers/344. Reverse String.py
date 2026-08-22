def search(s):
    n = len(s)
    i = 0
    j = n - 1
    while j > i:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
    return s

s = ["h","e","l","l","o"]
print(search(s))