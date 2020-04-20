all = list(map(int,input().split()))
tes = list(map(int,input().split()))
sc = 0
for i in range(len(all)):
    for j in range(len(tes)):
        if(all[i]== tes[j]):
            sc += max(all[i]*(i-j) ,(j-i)*all[i])
print(sc)