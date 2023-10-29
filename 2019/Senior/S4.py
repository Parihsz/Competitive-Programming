"""
we have N attractions (which must be visited in order), each with a score
we can vist up to K attractions each day
    and we want to visit all attractions in the fewest days possible
    math.ceil(N / K)
each day's score is the max score of the attractions vied that day
an entire schedule's score is the sum of each day's score

what is the highest score schedule possible
    we do not really need a schedule, just the score

the question is really jsut asking
    we have a set number of days
    the attractions are ordered
    the only thing we can allocate are spaces

what is the way to allocate the spaces into the set number of days
    such that the total score is highest
   
pretty classic math question lmao
"""
import itertools
import math

N, K = map(int, input().split())

attractions = [int(input()) for _ in range(N)]
days = int(math.ceil(N / K))
max_attractions_per_day = K
num_spaces = days * K - N
used_possibilities = set()
best_score = 0

for possibility in itertools.product(range(num_spaces + 1), repeat=(days - 1)):
    possibility = tuple(sorted(possibility))
    if possibility not in used_possibilities:
        allocated_spaces = []
        prev = 0
        for i in range(days - 1):
            allocated_spaces.append(possibility[i] - prev)
            prev = possibility[i]
        allocated_spaces.append(num_spaces - possibility[-1])
    daily_scores = []
    prev = 0
    for i in range(days):
        num_attractions = max_attractions_per_day - allocated_spaces[i]
        score = max(attractions[prev:prev + num_attractions])
        daily_scores.append(score)
        prev += num_attractions
    best_score = max(best_score, sum(daily_scores))
    
print(best_score)


