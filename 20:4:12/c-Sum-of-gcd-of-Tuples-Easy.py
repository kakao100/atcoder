import math
import itertools
import numpy as np
from sympy import prime
list2 = []
result = 0
n = int(input())

for i in range(1,n+1):
    if(not(prime(i))):
        for j in range(1,n):
          for k in range(1,n):
#            list2.append([i,j,k])
            result +=  np.gcd.reduce((i,j,k))
#            print(result ,i,k,j)
    else:
        result += (n*n)-1
for i in range(1,n+1):
    if(prime(i)):
        result += i
print(result)
#print(list2)