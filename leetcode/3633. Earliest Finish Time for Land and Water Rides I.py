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

#---------------------------------------------------------------------(run time 0ms)
"""def earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration):
        n = len(landStartTime)
        m = len(waterStartTime)

        minWaterEnd = min(waterStartTime[i] + waterDuration[i] for i in range(m))
        minLandEnd = min(landStartTime[i] + landDuration[i] for i in range(n))

        min_land_time = float("inf")
        for j in range(m):
            min_land_time = min(min_land_time, max(waterStartTime[j], minLandEnd) + waterDuration[j])
                
        min_water_time = float("inf")
        for j in range(n):
            min_water_time = min(min_water_time, max(landStartTime[j], minWaterEnd) + landDuration[j])

        return min(min_land_time, min_water_time)

landStartTime = [2,8]
landDuration = [4,1]
waterStartTime = [6]
waterDuration = [3]
res = earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration) 
print(res)"""