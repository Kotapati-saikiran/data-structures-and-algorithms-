def search(prices):
    i = 0 
    j = 1 
    best_answer = 0
    while j < len(prices):
        if prices[j] < prices[i]:
            i = j
            j += 1
        else:
            x = prices[j] - prices[i]
            best_answer = max(best_answer, x)
            j += 1
    return best_answer

prices = [7,1,5,3,6,4]
print(search(prices))