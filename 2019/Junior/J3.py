lines = int(input())
full_output = ""
for i in range(lines):
    equation = input()
    counter = 0
    prev = 0
    for i in range(len(equation)):
        if i == 0:
            prev = equation[i]
            counter += 1
        elif equation[i] == prev:
            counter += 1
        elif not equation[i] == prev:
            full_output += f"{counter} {prev} "
            counter = 1
            prev = equation[i]
        if i == len(equation)-1:
            full_output += f"{counter} {prev} "
    print(full_output)
    full_output = ""
       