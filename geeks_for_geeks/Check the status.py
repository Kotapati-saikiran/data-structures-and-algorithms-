a = 1
b = -1
flag = False
if a > 0 and b < 0 and flag == False:
    print(True)
elif a < 0 and b < 0 and flag == True :
    print(True)
elif a < 0 and b > 0 and flag == False:
    print(True)
elif a > 0 and b > 0 and flag == True:
    print(False)
else:
    print(False)