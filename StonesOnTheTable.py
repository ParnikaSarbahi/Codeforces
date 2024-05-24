n=int(input())
s=list(input())
c=0
while True:
    d=1
    for i in range(0,len(s)-1):
        if(s[i]==s[i+1]):
            s.pop(i+1)
            c+=1
            d=0
            break
    if(d==1):
        break
print(c)    
            
