def search(s, t):
    n = len(t)
    i = 0
    j = 0
    while i < len(s) and j <= n - 1:
        if s[i] == t[j]:
            flag = True
            i += 1
        j += 1
    if i == len(s):
        return True
    else:
        return False

s = "abc"
t = "ahbgdc"
print(search(s, t))