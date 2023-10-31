N, W, D = map(int, input().split())
# assuming no walkways for now
route = list(map(int, input().split()))
# with or without transformations, it is just the index difference 
#   of station N
for _ in range(D):
    a, b = map(int, input().split())
    temp = route[a-1]
    route[a-1] = route[b-1]
    route[b-1] = temp
    cost = route.index(N)
    print(cost)

    