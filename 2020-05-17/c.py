import math
a,b,h,m = map(int , input().split())
long_needle =(5 * m)/60 + h * 5  
sort_needle = m
ans = math.sqrt(a**2 + b **2 - 2*a*b*math.cos(abs(math.pi*(long_needle-sort_needle))/30))
print(ans)
