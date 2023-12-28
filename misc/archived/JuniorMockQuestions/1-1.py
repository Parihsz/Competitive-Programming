import itertools

C, N = map(int, input().split())
points = []
closest_three_points = []

for i in range(N):
    points.append(int(input()))

points.sort()

for i in itertools.combinations(points, 3):
    if sum(i) <= C:
        closest_three_points.append([C - sum(i), i[0], i[1], i[2]])
        
closest_three_points.sort()
print(closest_three_points[0][1], closest_three_points[0][2], closest_three_points[0][3])