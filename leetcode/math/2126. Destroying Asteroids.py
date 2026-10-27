mass = 10
asteroids = [3,9,19,5,21]
asteroids = sorted(asteroids)

for asteroid in asteroids:
    if mass < asteroid:
        print(False)
        break
    mass += asteroid
else:
    print(True)