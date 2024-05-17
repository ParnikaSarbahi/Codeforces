s=input()
u=0
l=0
for i in range(0,len(s)):
    if('A'<=s[i] and s[i]<='Z'):
        u=u+1
    else:
        l=l+1
if(u>l):
    print(s.upper())
elif(l>=u):
    print(s.lower())
