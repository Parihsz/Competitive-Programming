# Python 3.9.4, CCC Senior 4 2022
# Tested

N, C = map(int, input().split())

no_opposite = True
half = C // 2

if half == C / 2:
    no_opposite = False

points = tuple(map(int, input().split()))
locations = {}

for i, p in enumerate(points):
    if p not in locations:
        locations[p] = []
    locations[p].append(i)
successes = set()
for i, p in enumerate(points):
    other = p + half
    for i2, p2 in enumerate(points[i+1:]):
        i2 += i
        if p2 != p and (no_opposite or p2 != other % C):
            other2 = p2 + half
            a, b = sorted((other, other2))
            for p3 in range(a, b):
                p3 %= C
                for i3 in locations.get(p3, tuple()):
                    if i3 > i2:
                        successes.add((i, i2, i3))
                        
print(len(successes))