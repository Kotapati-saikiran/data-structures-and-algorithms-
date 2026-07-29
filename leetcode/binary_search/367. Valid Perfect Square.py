def search(num):
    flag = False
    l = 1
    h = num // 2
    while l <= h:
        mid = (l + h) // 2
        x = mid * mid
        if(x == num):
            flag = True
            break
        elif x < num:
            l = mid + 1
        else:
            h = mid - 1
    return flag
            
num = 16
print(search(num))