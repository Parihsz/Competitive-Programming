"""
Slow, and not very clever solution
Used to earn some quick marks when time is low
Full detaied solution will be up when I find motivation to write it

FYI, this solution takes 5 minutes to write, and can earn AT LEAST 4+ marks
"""

def check_vertical(puzzle, word):
    result = True

    if len(puzzle) != len(word):
        return False

    for l, c in zip(puzzle, word):
        for element in l:
            if element != c:
                result = False
                break 
        if not result:
            break  

    return result

word = input()
down = int(input())
over = int(input())
puzzle = []
count = 0

for i in range(down):
    data = input()
    dt = []
    for x in data:
        dt.append(x)
    puzzle.append(dt)

for i in range(len(puzzle)):
    if word in puzzle[i] or word[::-1] in puzzle[i]:
        count += 1
    if check_vertical(puzzle, word) or check_vertical(puzzle, word[::-1]):
        count += 1
    
    
