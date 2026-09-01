def search(height):
    n = len(height)
    i = 0
    j = n - 1
    best_answer = 0
    while j > i:
        width = j - i
        if height[i] <= height[j]:
            area = height[i] * width
            best_answer = max(area, best_answer)
            i += 1
        else:
            area = height[j] * width
            best_answer = max(area, best_answer)
            j -= 1
    return best_answer

height = [1,8,6,2,5,4,8,3,7]
print(search(height))