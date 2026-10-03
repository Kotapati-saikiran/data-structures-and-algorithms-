def search(s, p):
    map1 = {}


    for ch in p:
        if ch in map1:
            map1[ch] += 1
        else:
            map1[ch] = 1

    map2 = {}

    l = 0
    r = len(p) - 1
    array = []


    for ch in s[l:r + 1]:
        if ch in map1:
            if ch in map2:
                map2[ch] += 1
            else:
                map2[ch] = 1

    while r < len(s):


        if map1 == map2:
            array.append(l)


        left_char = s[l]

        if left_char in map2:
            map2[left_char] -= 1

            if map2[left_char] == 0:
                del map2[left_char]


        l += 1
        r += 1


        if r < len(s):
            right_char = s[r]

            if right_char in map1:
                if right_char in map2:
                    map2[right_char] += 1
                else:
                    map2[right_char] = 1

    return array


s = "cbaebabacd"
p = "abc"

print(search(s, p))