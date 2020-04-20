n,m = map(int,input().split())
all = list(map(int,input().split()))
result = 0

for i in range(m):
    result += all[i]

result = max(-1 ,n-(result))
print(result)