import numpy as np
print("test")
str = input()
num = str.split()
hight = int(num[0])
width = int(num[1])
list  =[]
for i in range(int(hight)): 
    tem = input()
    for j in range(int(len(tem))):
      list.append(tem[j])    
print(list)
list2 = np.array(list)
list2 = list2.reshape(width, hight)
print(list2)


