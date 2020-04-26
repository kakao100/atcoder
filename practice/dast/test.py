str = input()

if(len(str)%2 != 0):
    print("No")
    exit()
for i in range(len(str)):
    if(i % 2 == 0):
        if(str[i]!='h'):
            print("No")
            exit()
    if(i % 2 == 1):
        if(str[i]!='i'):
            print("No")
            exit()
print("Yes")