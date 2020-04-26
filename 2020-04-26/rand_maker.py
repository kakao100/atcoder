import random
s = ""
for i in range(200000):
    s = s + str(random.randint(1,9))

n = s
n_len=len(s)

count = 0
for cut_length in range(4,n_len + 1):
    for first in range(0,n_len - cut_length + 1):
        cuted_num = int(n[first:first + cut_length])
        if(cuted_num % 2019 == 0):
            count += 1
print(count)