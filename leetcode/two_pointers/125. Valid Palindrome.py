def search(s):
    if len(s) == 1:
        return True
    s = s.lower()
    r = ''.join(ch for ch in s if ch.isalnum())
    n = len(r)
    flag = False
    i = 0
    j = n - 1
    if n == 0:
        return True
    while i <= n -1 and j >= 0:
        if r[i] != r[j]:
            flag = False
            break
        else:
            flag = True
            i += 1
            j -= 1
    return flag
    
s = ".,"
print(search(s))