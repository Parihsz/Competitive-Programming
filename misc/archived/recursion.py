def double(num):
    if num == 524288:
        return num
    else:
        print(num)
        return double(num*2)
    
double(1)