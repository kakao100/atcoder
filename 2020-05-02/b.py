x = int(input())
sum = 100
i = 0
while(True):
    if(sum >= x):
        print(i)
        exit()
    i += 1
    sum = int(sum  * 1.01)