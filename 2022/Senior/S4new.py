# Python 3.9.4, CCC Senior 4 2022
# Tested

"""
given a sequence of points along a circle 
determine (print) the number of good triplets 
good triplets are set of three points which
    contain the center of the circle within it

"""
import itertools 

points = []
count = 0

def angle_test(angle, start, end):
    """
    test whether angle is between start and end, exclusive
    kind of tricky
    """
    while angle < start:
        angle += C
    return angle < end

def test_good_triplets(a, b, c, points, C):
    """
    a b c are good if
        b and c lie on different sides of the circle, divided by a and a_opposite
    """
    if C % 2==0:
        A_opposite = a + C // 2
        B_range = (points[a], A_opposite)
        C_range = (A_opposite, points[a])
    else:
        A_opposite_for_C = points[a] + C // 2
        A_opposite_for_B = A_opposite_for_C + 1
        B_range = (points[a], A_opposite_for_B)
        C_range = (A_opposite_for_C, points[a])
    return angle_test(points[b], *B_range) and angle_test(points[c], *C_range)

N, C = map(int, input().split())

for _ in range(N):
    points.append(int(input()))

for a, b, c in itertools.combinations(range(N), 3):
    if test_good_triplets(a, b, c, points, C):
        count += 1
print(count)


