n = int(input())
all = list(map(int,input().split()))
result = 0
while(True):
    for i in range(n):
        if(all[i] % 2 ==1 or all[i]==0):
            print(result)
            exit()
    result += 1
    all = list(map(lambda x:x//2,all))

