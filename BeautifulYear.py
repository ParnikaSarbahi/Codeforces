s=str(int(input())+1)
c=0
while(c==0):
    for i in s:
        c=1
        if s.count(i)!=1:
            c=0
            s=str(int(s)+1)
            break
print(s)
