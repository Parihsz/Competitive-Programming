direction = ""
previous_direction = ""
while True:
    new = input()
    if new == "99999":
        exit()
    sum = 0
    sum = int(new[0]) + int(new[1])
    if sum % 2 == 0: 
        if not sum == 0:
            direction = "right"
            previous_direction = direction
        else:
            direction = previous_direction
    else:
        direction = "left"
        previous_direction = direction
    print(direction + " " + new[2] + new[3] + new[4])
    