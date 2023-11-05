N, M = map(int, input().split())
grid = []
islands = []
def get_islands():
    visited = [[False]*M for _ in range(N)]

    def search(r, c):
        if (r >= 0 and r < N and c >= 0 and c < M and not visited[r][c] and grid[r][c] == "1"):
            visited[r][c] = True
            search(r, c + 1)
            search(r, c -1)
            search(r + 1, c)
            search(r - 1, c)
        return
    
    for r in range(N):
        for c in range(M):
            if grid[r][c] == "1" and not visited[r][c]:
                search(r, c)
                islands.append(str(r) + " " + str(c))


for i in range(N):
    row = input()
    grid.append(row)

get_islands()

for island in islands:
    print(island)