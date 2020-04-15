s = input()
t = ""
a = "dream" 
b = "dreamer" 
c = "erase"
d = "eraser"
s= s.replace("drea"," drea")
s= s.replace("eras"," eras")
s= s.replace(b," ")
s= s.replace(a," ")
s= s.replace(d," ")
s= s.replace(c," ")
s= s.replace(" ","")
if(len(s)==0):
    print("YES")
else:
    print("NO")

