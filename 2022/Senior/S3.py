# Python 3.9.4, CCC Senior 3 2022
# Untested

def count_good_samples(n, composition):
    count = 0
    for i in range(n):
        s = set()
        for j in range(i, n):
            if composition[j] in s: 
                break
            s.add(composition[j])
            count += 1
    return count

def compose(n, m, k):
    if m == 1:
        return [1] * n if k == n else [-1]
    elif m == 2:
        for i in range(n + 1):
            composition = [1] * i + [2] * (n - i)
            if count_good_samples(n, composition) == k:
                return composition
    else:
        composition = list(range(1, m + 1)) + [m] * (n - m)
        
        while count_good_samples(n, composition) != k:
            for i in range(n - 1, -1, -1):  
                if composition[i] < m:
                    composition[i] += 1
                    composition[i+1:] = [1] * (n - i - 1)
                    break
            else: 
                return [-1]

        return composition

    return [-1]

n, m, k = map(int, input().split())
print(*compose(n, m, k))

