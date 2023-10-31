c = int(input())
row1 = list(map(int, input().split()))
row2 = list(map(int, input().split()))
tape = 0


for i in range(len(row1)):
    if i == c - 1: # we are at the end
        if row1[i] == 1:
            if row1[i] == row2[0]:
                tape += 4
            else:
                tape += 3
            if row1[i-1] == 1:
                tape -= 1
    elif i == 0:
        if row1[i] == 1:
           if row1[i] == row2[0]:
              tape += 4
           else:
              tape += 3
           if row1[i+1] == 1:
              tape -= 1
    else:
        if row1[i] == 1:
            if i % 2 == 0:
                if row1[i] == row2[2]:
                    tape += 4
                else:
                    tape += 3
                if row1[i+1] == 1:
                    tape -= 1
                if row1[i-1] == 1:
                    tape -= 1
            else:
                tape += 3
                if row1[i+1] == 1:
                    tape -= 1
                if row1[i-1] == 1:
                    tape -= 1
      
for i in range(len(row2)):
    if i == c - 1: # we are at the end
        if row2[i] == 1:
            if row2[i] == row1[i]:
                continue
            else:
                tape += 3
            if row2[i-1] == 1:
                tape -= 1
    elif i == 0:
        if row2[i] == 1:
           if row2[i] == row1[i]:
              continue
           else:
              tape += 3
           if row2[i+1] == 1:
              tape -= 1
    else:
        if row2[i] == 1:
            if i % 2 == 0:
                if row2[i] == row1[i]:
                    continue
                else:
                    tape += 3
                if row2[i+1] == 1:
                    tape -= 1
                if row2[i-1] == 1:
                    tape -= 1
            else:
                tape += 3
                if row2[i+1] == 1:
                    tape -= 1
                if row2[i-1] == 1:
                    tape -= 1
                    
print(tape)

    