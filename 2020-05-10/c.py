import numpy as np
n,m,x = map(int,input().split())
all = []
cost = []
result = []
for i in range(n):
    tmp =list(map(int,input().split()))
    all.append(tmp[1:])
    cost.append(tmp[0])
# print(cost)
# print(all)
for i1 in range(m):
    for i2 in range(i1+1,n):
        sum = np.array(all[i1]) +np.array(all[i2])
        flag = True
        for i in sum:
            if(i < x):
                flag = False
        if(flag):
            result.append(cost[i1]+cost[i2])

#3
for i1 in range(n):
    for i2 in range(i1+1,n):
        for i3 in range(i2+1,n):
            sum = np.array(all[i1]) + np.array(all[i2]) + np.array(all[i3]) 
            flag = True
            for i in sum:
                if(i < x):
                    flag = False
            if(flag):
                result.append(cost[i1]+cost[i2]+cost[i3])
#4
for i1 in range(m):
    for i2 in range(i1+1,n):
        for i3 in range(i2+1,n):
                for i4 in range(i3+1,n):
                    sum = np.array(all[i1]) + np.array(all[i2]) + np.array(all[i3])+np.array(all[i4])
                    flag = True
                    for i in sum:
                        if(i < x):
                            flag = False
                    if(flag):
                        result.append(cost[i1]+cost[i2]+cost[i3]+cost[i4])
for i1 in range(m):
    for i2 in range(i1+1,n):
        for i3 in range(i2+1,n):
            for i4 in range(i3+1,n):
                for i5 in range(i4+1,n):
                    sum = np.array(all[i1]) + np.array(all[i2]) + np.array(all[i3])+np.array(all[i4])+np.array(all[i5])
                    flag = True
                    for i in sum:
                        if(i < x):
                            flag = False
                    if(flag):
                        result.append(cost[i1]+cost[i2]+cost[i3]+cost[i4]+cost[i5])
for i1 in range(m):
    for i2 in range(i1+1,n):
        for i3 in range(i2+1,n):
            for i4 in range(i3+1,n):
                for i5 in range(i4+1,n):
                    for i6 in range(i5+1,n):
                        
                        sum = np.array(all[i1]) + np.array(all[i2]) + np.array(all[i3])+np.array(all[i4])+np.array(all[i5])+np.array(all[i6])
                        
                        flag = True
                        for i in sum:
                            if(i < x):
                                flag = False
                        if(flag):
                            result.append(cost[i1]+cost[i2]+cost[i3]+cost[i4]+cost[i5]+cost[i6])
for i1 in range(m):
    for i2 in range(i1+1,n):
        for i3 in range(i2+1,n):
            for i4 in range(i3+1,n):
                for i5 in range(i4+1,n):
                    for i6 in range(i5+1,n):
                        for i7 in range(i6+1,n):
                            sum = np.array(all[i1]) + np.array(all[i2]) + np.array(all[i3])+np.array(all[i4])+np.array(all[i5])+np.array(all[i6])+np.array(all[i7])
                            flag = True
                            for i in sum:
                                if(i < x):
                                    flag = False
                            if(flag):
                                result.append(cost[i1]+cost[i2]+cost[i3]+cost[i4]+cost[i5]+cost[i6]+cost[i7])

for i1 in range(m):
    for i2 in range(i1+1,n):
        for i3 in range(i2+1,n):
            for i4 in range(i3+1,n):
                for i5 in range(i4+1,n):
                    for i6 in range(i5+1,n):
                        for i7 in range(i6+1,n):
                            sum = np.array(all[i1]) + np.array(all[i2]) + np.array(all[i3])+np.array(all[i4])+np.array(all[i5])+np.array(all[i6])+np.array(all[i7])
                            #print(i1,i2,i3,i4,i5,i6,i7,sum)
                            flag = True
                            for i in sum:
                                if(i < x):
                                    flag = False
                            if(flag):
                                result.append(cost[i1]+cost[i2]+cost[i3]+cost[i4]+cost[i5]+cost[i6]+cost[i7])

for i1 in range(m):
    for i2 in range(i1+1,n):
        for i3 in range(i2+1,n):
            for i4 in range(i3+1,n):
                for i5 in range(i4+1,n):
                    for i6 in range(i5+1,n):
                        for i7 in range(i6+1,n):
                            for i8 in range(i7+1,n):
                                sum = np.array(all[i1]) + np.array(all[i2]) + np.array(all[i3])+np.array(all[i4])+np.array(all[i5])+np.array(all[i6])+np.array(all[i7])+np.array(all[i8])
                                #print(i1,i2,i3,i4,i5,i6,i7,sum)
                                flag = True
                                for i in sum:
                                    if(i < x):
                                        flag = False
                                if(flag):
                                    result.append(cost[i1]+cost[i2]+cost[i3]+cost[i4]+cost[i5]+cost[i6]+cost[i7]+cost[i8])



if(result ==[]):
    print(-1)
else:
    print(min(result))