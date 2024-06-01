n=int(input())
c=1
s=input()
for i in range(n-1):
    s1=input()
    if(s[1]==s1[0]):
        c+=1
    s=s1
print(c)
