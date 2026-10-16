def search(fruits):
    n = len(fruits)
    left = 0
    right = 0
    valid_window = 2
    best_answer = 0
    freq = {}
    while right < n:
        
        if len(freq) <= valid_window:
            
            if fruits[right] in freq:
                freq[fruits[right]] += 1
            else:
                freq[fruits[right]] = 1
            right += 1
            
        while len(freq) > valid_window:
            freq[fruits[left]] -= 1
            if freq[fruits[left]] == 0:
                del freq[fruits[left]]
            left += 1
        best_answer = max(best_answer, right - left)
    return best_answer

fruits = [1,2,3,2,2]
print(search(fruits))

#-------------------------------------------------------------------(Usinf for loop)
"""def search(fruits):
    left = 0
    valid_window = 2
    best_answer = 0
    freq = {}

    for right in range(len(fruits)):
        if fruits[right] in freq:
            freq[fruits[right]] += 1
        else:
            freq[fruits[right]] = 1

        while len(freq) > valid_window:
            freq[fruits[left]] -= 1

            if freq[fruits[left]] == 0:
                del freq[fruits[left]]

            left += 1

        best_answer = max(best_answer, right - left + 1)

    return best_answer


fruits = [1, 2, 3, 2, 2]
print(search(fruits))""" 