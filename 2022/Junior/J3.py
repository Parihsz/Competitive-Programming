tune = input()
output = ""
tuned_index = 99999999
for x in range(len(tune)):
    i = tune[x]
    if i == "+":
        output += " tighten "
        tuned_index = x
    elif i == "-":
        output += " loosen "
        tuned_index = x
    else:
        if tuned_index + 1 == x:
            output += i
            output += "\n" 
        else:
            output += i
print(output)