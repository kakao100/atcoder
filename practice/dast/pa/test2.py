count = 0
for i in range(1,7):
    for j in range(1,7):
        a = i + j
        if(a % 3 == 0):
            count += 1
print(count)
