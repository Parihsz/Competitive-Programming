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
