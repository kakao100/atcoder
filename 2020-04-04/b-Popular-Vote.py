cl1 = input().split()
cl2 = input().split()
n = int(cl1[0])
m = int(cl1[1])
cl1 = [int(s) for s in cl1]
cl2 = [int(s) for s in cl2]
sum= 0.0
for i in range(n):
    sum = cl2[i]+ sum
cl2 = sorted(cl2,reverse=True)
if(cl2[m-1] < sum/(4*m)):
    print("No")
else:
    print("Yes")