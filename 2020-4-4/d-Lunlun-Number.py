num = int(input())
count = 0
def check(x):
    f= True
    if(x < 10):
        return True
    x = str(x)
    for i in range(len(x)-1):
        if( int(x[i]) - int(x[i + 1]) != 0):
            f = False
        if( int(x[i]) - int(x[i + 1]) != 1 ):
            f = False
        if( int(x[i]) - int(x[i + 1]) != -1 ):
            f = False
        if(f == False):
            return False
    return True
i = 0    
while(True):
    i = i + 1
    if(check(i)):
    #    print(i)
        count = count + 1 
        if(count == num ):
            print(i)
            exit()
        
