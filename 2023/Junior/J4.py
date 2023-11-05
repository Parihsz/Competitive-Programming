# contributed by @Eric Tan
c=int(input())
top=[]
bottom=[]
top=input()
top=top.split()
bottom=input()
bottom=bottom.split()

tape=0
for i in range(c):
    if top[i]=='1':
        tape+=3
    if bottom[i]=='1':
        tape+=3
    if top[i]=='1' and bottom[i]=='1' and i%2==0:
        tape-=2

for o in range(c-1):
    if top[o]=='1' and top[o+1]=='1':
        tape-=2
    if bottom[o]=='1' and bottom[o+1]=='1':
        tape-=2
print(tape)