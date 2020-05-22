a,b,c,k = map(int,input().split())
count = 0
if(a > k):
    count = k
elif(a + b > k):
    count = a
else:
    tmp = k -(a + b)
    count = a - tmp
print(count)