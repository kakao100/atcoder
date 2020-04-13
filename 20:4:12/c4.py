import math
import itertools
import numpy as np
n = int(input())
result =0
all = []
for i in range(1,n+1):
    for j in range(1,i):
        a = math.gcd(i,j)
        result += a*2
        all.append(a)
j = 1

for i in all:
    for j in range(n):
        result +=math.gcd(i,j)*2
  
print(result)