S=input()
p=2019
h=0
d=1
t=0
c=[0]*p
c[0]=1
for s in reversed(S):
  m=int(s)*d%p
  h=(h+m)%p
  t+=c[h]
  c[h]+=1
  d=d*10%p
print(t)