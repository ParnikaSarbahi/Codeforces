s=input()
s1=s.split()
n=int(s1[0])
k=int(s1[1])
for i in range(k):
    if(n%10!=0):
        n-=1
    else:
        n=n//10
print(n)
