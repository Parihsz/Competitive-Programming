from collections import deque
#classic BFS method, unweighted graph since all edges are cost 1

def find_path(connections, start, end):
    prevs = {start: start}
    q = deque((start, ))
    while len(q) > 0:
        current = q.popleft()
        if current == end:
            path = []
            prev = current
            while prev != start:
                path.append(prev)
                prev = prevs[prev]
            path.append(start)
            return path
        for next in connections[current]:
            if next not in prevs:
                prevs[next] = current
                q.append(next)

N, W, D = map(int, input().split())
walks = {x : set() for x in range(1, N + 1)}
route = list(map(int, input().split()))

for _ in range(W):
    a, b = map(int, input().split())
    walks[a].add(b)
route = list(map(int, input().split()))

for _ in range(D):
    a, b = map(int, input().split())
    temp = route[a-1]
    route[a-1] = route[b-1]
    route[b-1] = temp
    connections = walks.copy()
    for i in range(len(route) - 1):
        connections[route[i]].add(route[i+1])
    path = find_path(connections, 1, N)
    print(len(path))


    