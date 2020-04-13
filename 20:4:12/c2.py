import math
import itertools
import numpy as np
n = int(input())
result = 0
list2 = list(range(1,n+1))
all = list(itertools.combinations_with_replacement(list2, 3))
for i in all:
    if(i[0]==i[1] and i[0]==i[2]):
        result += np.gcd.reduce(i)
    elif (i[0]==i[1] or i[0]==i[2] or i[1]==i[2]):
        result += np.gcd.reduce(i)*3
    else:
        result += np.gcd.reduce(i)*6
print(all)
print(result)
