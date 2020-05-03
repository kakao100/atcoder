a,b,n = map(int,input().split())
width = 1000
all = []
for x in range(1,min(width,n)):
    ans = int((a * x) // b)  - a * int(x // b) 
    all.append(ans)

for x in range(n,max(n -width,0) ,-1):
    ans = int((a * x) // b)  - a * int(x // b) 
    all.append(ans)

print(max(all))