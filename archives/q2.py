max_weight = int(input())
number_of_cars = int(input())

cars = []
weight = 0


for i in range(number_of_cars):
    cars.append(int(input()))

for i in range(len(cars)):
    weight += cars[i]
    if weight > max_weight:
        if i == 0:
            print(0)
        else:
            print(i+1)
        exit()