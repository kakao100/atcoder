cl1 = input().split()
cl1 = [int(s) for s in cl1]
x = cl1[0]
k = cl1[1]

a = x % k
b = -(x % k - k)
print(min(a,b))

#517061501112