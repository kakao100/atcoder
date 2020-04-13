import math
import itertools
list2 = [1,2,3]
p_list = list(itertools.combinations(list2, 2))
print(p_list)
#[(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
print(len(p_list))
print(p_list[0][1])
#2
for v in itertools.combinations(list2,2):
    print(v)
# (1, 2)
# (1, 3)
# (2, 1)
# (2, 3)
# (3, 1)
# (3, 2)
# # v[0]やv[1]で各要素を呼ぶことも可能
for v in itertools.combinations(list2,2):
    print(v[0])


