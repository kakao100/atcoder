import math
import itertools
import numpy as np
from sympy import prime
n = int(input())
result = 0
wlist=[]
list2 = list(range(1,n+1))
all = list(itertools.combinations_with_replacement(list2, 2))
for i in all:
    wlist.append(np.gcd.reduce(i))
    
print(all)
print(result)
