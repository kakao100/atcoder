n =int(input())
now_x = 0
now_y = 0 
now_t = 0
for i in range(n):
    t,x,y= map(int,input().split())
    x2 = x -now_x
    y2 = y -now_y
    t2 = t -now_t
    distance = abs(x2) + abs(y2)
    if( not(distance <= t2 and (distance - t2)%2 ==0)):
        print("No")
        exit()
    now_x = x
    now_y = y
    now_t = t
print("Yes")
