def search(people, limit):
    people.sort()
    lightest = 0
    heaviest = len(people) - 1
    count = 0
    while lightest <= heaviest:
        sum_of_people = people[lightest] + people[heaviest]
        
        if sum_of_people <= limit:
            lightest += 1
            heaviest -= 1
            count += 1
        elif sum_of_people > limit:
            heaviest -= 1
            count += 1
    return count
    

people = [3,2,2,1]
limit = 3
print(search(people, limit))