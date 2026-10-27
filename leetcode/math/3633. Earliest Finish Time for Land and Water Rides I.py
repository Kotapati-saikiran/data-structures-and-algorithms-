lst = [2,8]
ld = [4,1]
wst = [6]
wd = [3]

ans = float('inf')
for i in range(len(lst)):
    for j in range(len(wst)):

        #Land to water
        land_finish = lst[i] + ld[i]
        water_start = max(land_finish, wst[j])
        water_finish = water_start + wd[j]
        ans = min(ans, water_finish)

        #water to land
        water_finish = wst[j] + wd[j]
        land_start = max(water_finish,lst[i])
        land_finish = land_start + ld[i]
        ans = min(ans,land_finish)
print(ans)
