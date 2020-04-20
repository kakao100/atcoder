n = int(input())
all = list(map(int,input().split()))
result ={}
for i in range(n):
    result[i] = 0

for i in all:
    result[i-1] += 1

#print(result)
for i in range(n):
    print(result[i])


