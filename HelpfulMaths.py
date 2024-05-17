s1=input()
l=[]
for i in s1:
    if(i.isdigit()):
        l.append(i)
l.sort()
le=len(l)
for i in range(0,le):
    if(i!=(le-1)):
        print(l[i]+"+",end="")
    else:
        print(l[i])
