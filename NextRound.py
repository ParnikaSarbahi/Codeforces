s=input()
s1=s.split()
n=int(s1[0])
k=int(s1[1])
c=input()
c1=c.split()
a=int(c1[k-1])
p=0
for i in range(0,n):
    if(int(c1[i])!=0):
        if(int(c1[i])>=a):
            p=p+1
print(p)
