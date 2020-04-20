n,k = map(int,input().split())
num  = 0
for select_num in range(k,n+2):
    st = (select_num*(2*0+(select_num - 1)*( 1)))/2
    ed = (select_num*(2*n+(select_num - 1)*(-1)))/2
    sum = ed - st + 1
    num += sum
print(int(num)%1000000007)

