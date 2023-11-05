"""
class was divided into groups of 3
there are 2 constraints:
some students must work together in the same group
some students must work together in seperate groups
your job is to determine how many constraints are violated

the input:
1st line is integer X
next X lines will be 2 names, which re students that must be in the same group

then the next line is integer Y
there will then be Y lines of which students must NOT be in the same group

next line will be integer G
next G lines will be 3 different names, which are 3 students that have been placed in the same group

^
Summary of the question. A summary/rephrase is crutial with question that have lots of text but no visualization.
"""

X = int(input())
violation = 0
must_together = []
must_seperate = []
groups = []

for i in range(X):
    must_together.append(input().split())

Y = int(input())
for i in range(Y):
    must_seperate.append(input().split())
    
Z = int(input())
for i in range(Z):
    groups.append(input().split())

already_violated = []

def check_together(first_student, second_student, third_student, together):
    if first_student in together:
        if (not second_student in together) and (not third_student in together):
            return True
    if second_student in together:
        if (not third_student in together) and (not first_student in together):
            return True
    if third_student in together:
        if (not second_student in together) and (not first_student in together):
            return True
        
def check_seperate(first_student, second_student, third_student, together):
    if first_student in together:
        if (second_student in together) or (third_student in together):
            return True
    if second_student in together:
        if (third_student in together) or (first_student in together):
            return True
    if third_student in together:
        if (second_student in together) or (first_student in together):
            return True   
        

for group in groups:
    for friends in must_together:
        if check_together(group[0], group[1], group[2], friends):
            if friends not in already_violated:
                already_violated.append(friends)
                violation += 1
    for enemies in must_seperate:
        if check_seperate(group[0], group[1], group[2], enemies):
            if enemies not in already_violated:
                already_violated.append(enemies)
                violation += 1

print(violation)

"""
this solution is logic based, and super slow
this would get 14/15 on the actual CCC.
"""