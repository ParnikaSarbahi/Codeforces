s=input()
s1=s.split()
n=int(s1[0])
h=int(s1[1])
s=input()
w=0
s2=s.split()
for i in s2:
    if(int(i)>h):
        w=w+2
    else:
        w=w+1
print(w)
