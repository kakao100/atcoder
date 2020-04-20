max_num = 0
n = int(input())
all = list(map(int,input().split()))
st = list(range(1,n+1))
dic = {}
for i in range(len(all)):
    dic[i]= all[i]
dic= sorted(dic.items(), key=lambda x:x[1],reverse=True)
for i in dic:
    mi = min(st)
    ma = max(st)
    te = i.key
    remo= max_ju(abs(te-min),abs(te-max))
    st
print(dic)