n = input()
count = 0 
for i in range(1,10**2000):
    count += n.count(str(2019*i))
print(count)