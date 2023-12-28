sizes = {"S": 1, "M": 2, "L": 3}
J = int(input())
A = int(input())

jerseys = {}
for _ in range(J):
    size, number = input().split()
    jerseys[int(number)] = sizes[size]

satisfied = 0
for _ in range(A):
    size, number = input().split()
    if jerseys[int(number)] >= sizes[size]:
        satisfied += 1
        jerseys[int(number)] = 0

print(satisfied)