import itertools

points = []
count = 0

def is_angle_within_bounds(angle, start, end, circle_circumference):
    while angle < start:
        angle += circle_circumference
    return angle < end

def are_points_good_triplets(index_a, index_b, index_c, points_list, circle_circumference):
    if circle_circumference % 2 == 0:
        a_opposite = index_a + circle_circumference // 2
        b_bounds = (points_list[index_a], a_opposite)
        c_bounds = (a_opposite, points_list[index_a])
    else:
        a_opposite_for_c = points_list[index_a] + circle_circumference // 2
        a_opposite_for_b = a_opposite_for_c + 1
        b_bounds = (points_list[index_a], a_opposite_for_b)
        c_bounds = (a_opposite_for_c, points_list[index_a])
    return is_angle_within_bounds(points_list[index_b], *b_bounds, circle_circumference) and \
           is_angle_within_bounds(points_list[index_c], *c_bounds, circle_circumference)

N, C = map(int, input().split())

for _ in range(N):
    point_angle = int(input())
    points.append(point_angle)

for a, b, c in itertools.combinations(range(N), 3):
    if are_points_good_triplets(a, b, c, points, C):
        count += 1 
