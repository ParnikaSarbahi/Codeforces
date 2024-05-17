n=int(input())
x=0
l=[]
for i in range(n):
    a=input()
    l.append(a)
for t in l:
    if(t[0]=='X'):
        if(t[1]=='-'):
            x=x-1
        elif(t[1]=='+'):
            x=x+1
    elif(t[0]=='-'):
        x=x-1
    elif(t[0]=='+'):
        x=x+1
print(x)
