grid = ['1','2','3','4']
instructions = input()
for i in instructions:
    if i == "H":
        old0 = grid[0]
        old1 = grid[1]
        old2 = grid[2]
        old3 = grid[3]
        grid[0] = old2
        grid[1] = old3
        grid[2] = old0
        grid[3] = old1
    elif i == "V":
        old0 = grid[0]
        old1 = grid[1]
        old2 = grid[2]
        old3 = grid[3]
        grid[0] = old1
        grid[1] = old0
        grid[2] = old3
        grid[3] = old2
print(grid[0] + " " + grid[1] + "\n" + grid[2] + " " + grid[3])
