a,b,c,n = map(int,input().split())
all = {}
all[1] = [0,0,0]
de = 40
for i in range(de):
    for j in range(de):
        for k in range(de):
            all[a**i * b**j * c**k] = [i,j,k]

all =sorted(all.items())
#for i in all:
#    print(i)
#print(all[n-1])
print(all[n-1][0])
