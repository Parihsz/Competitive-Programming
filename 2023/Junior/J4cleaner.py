# parse inputs
x = int(input())
top = input().split()
bottom = input().split()

# choose data structures, and define variables
tape = 0

# apply algorithms
for i in range(x):
    if top[i] == "1":
        tape += 3
    if bottom[i] == "1":
        tape += 3
    if top[i] == bottom[i] and top[i] == "1" and i % 2 == 0:
        tape -= 2
for i in range(x-1):
    if top[i] == "1" and top[i+1] == "1":
        tape -= 2
    if bottom[i] == "1" and bottom[i+1] == "1":
        tape -= 2

#output result
print(tape)
