n=int(input())
l=[]
for i in range(n):
    a=input()
    l.append(a)
for i in l:
    if(len(i)<=10):
        print(i)
    else:
        print(i[0]+str(len(i)-2)+i[len(i)-1])
