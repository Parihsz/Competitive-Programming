word = input()
other = input()

cyclic_shifts = []

def get_cyclic_shifts(w, currentIteration):
    if currentIteration > len(w):
        return
    new = ''
    for i in range(len(w)):
        if i == 0:
            continue
        else:
            new += w[i]
    new += w[0]
    cyclic_shifts.append(new)
    get_cyclic_shifts(new, currentIteration+1)

get_cyclic_shifts(other, 1)

for i in cyclic_shifts:
    if i in word:
        print("yes")
        exit()
    
print("no")