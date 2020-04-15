n =int(input())
all=[]
for i in range(n):
    a = int(input())
    if(not (a in all)):
        all.append(a)

print(len(all))