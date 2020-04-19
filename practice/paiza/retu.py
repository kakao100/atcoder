a,b,c,k = map(int,input().split())
count = 0
num = 0
while(True):
    num += 1
    test = num
    while(test % a == 0):
        test = test // a
    while(test % b == 0):
        test = test // b
    while(test % c == 0):
        test = test // c
    if(test == 1):
        count += 1 
    if(count == k):
        break        
print(num)