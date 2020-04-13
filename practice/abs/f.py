n,a,b = map(int ,input().split())

result = 0
for i in range(1,n+1):
    sum=0
    for j in str(i):
        sum += int(j)
    if(a <= sum and sum <=b):
        result += i

print(result)

