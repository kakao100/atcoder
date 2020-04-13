
import itertools
count = 0
str = input()
list = str.split()
str1 = input()
list1 = str1.split()
for v in itertools.combinations(list1, 3):
    if(int(v[0])+int(v[1])+int(v[2]) == int(list[1])):
      count = count + 1
print(count)
