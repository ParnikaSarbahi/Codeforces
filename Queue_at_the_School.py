i=input()
n,t=i.split()
s=list(input())
for i in range(int(t)):
    pob=[]
    for i in range(len(s)-1):
        if s[i]=='B':
            pob.append(i)
    for i in pob:
        c=s[i]
        s[i]=s[i+1]
        s[i+1]=c
print(''.join(s))
