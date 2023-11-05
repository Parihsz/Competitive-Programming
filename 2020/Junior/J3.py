"""
pretty interesting question Art.
"""

drops = int(input())
paints = []
for i in range(drops):
    parts = [part.strip() for part in input().split(',')]
    result_list = (int(parts[0]), int(parts[1]))
    paints.append(result_list)

max_x = 0
max_y = 0
min_x = 1000
min_y = 1000
for i in paints:
    if i[0] > max_x:
        max_x = i[0]
for i in paints:
    if i[1] > max_y:
        max_y = i[1]
for i in paints:
    if i[0] < min_x:
        min_x = i[0]
for i in paints:
    if i[1] < min_y:
        min_y = i[1]

first = str(min_x-1) + "," + " " + str(min_y-1)
second = str(max_x+1) + "," + " " + str(max_y+1)

print(first)
print(second)