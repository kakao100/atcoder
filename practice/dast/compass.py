atk = 629
atk2 = 700
# フルカノイエガブ160
atk3 = 699
huru = 3.8
siryu = 3.72
ada = 1.3
ada_av = 1.2
ruru = 1.35

print("adamu-------")
a = atk *ada * huru 
b = atk *ada * siryu * ada_av 
print(a,b,a+b) 
a = atk2 *ada * huru
b = atk2 *ada * siryu * ada_av
print(a,b,a+b)
print("ruru--------")
a = atk *ruru * huru
b = atk *ruru * siryu 
print(a,b,a+b)
a = atk2 *ruru * huru
b = atk2 *ruru * siryu
print(a,b,a+b)
