def search(g,s):
    g.sort()
    s.sort()
    c = 0
    i = 0
    j = 0
    best_answer = 0
    while i <len(g) and j < len(s):
        if s[j] >= g[i]:
            c += 1
            i += 1
            j += 1
        else:
            c = 0
            j += 1
        best_answer = max(best_answer, c)
    return best_answer

  
g = [1,2,3]
s = [1,1]
print(search(g,s))