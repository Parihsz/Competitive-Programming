"""
I did j3 during the CCC this year, and the solution was super dumb since i was rushing. 
This is the less dumb version, as the old one was VERY not scalable and also slow
"""
people = int(input())
availability = []
same = []
counts = [0]*5

for i in range(people):
    availability.append([])
    avail = input()
    for x in range(len(avail)):
        availability[i].append(avail[x])

for person_avail in availability:
    for day, avail in enumerate(person_avail):
        if avail == 'Y':
            counts[day] += 1

most = max(counts)

for i in range(len(counts)):
    print(counts[i])
    if counts[i] == most:
        same.append(i+1)

print(','.join(map(str, same)))

"""
This new solution is better and scalable
It is still quite dumb, but I really don't have the motivation to actually make it good
"""