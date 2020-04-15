n = int(input())
all = list(map(int,input().split()))

all.sort(reverse=True)
#print(all)
a = 0
b = 0
for i in range(len(all)):
    if(i%2 ==0):
        a+= all[i]
    else:
        b += all[i]
print(a-b)


