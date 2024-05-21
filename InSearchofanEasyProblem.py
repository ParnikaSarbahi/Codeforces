n=int(input())
i=input()
l=i.split()
c=0
for i in l:
    if(int(i)==1):
        c=1
        break
if(c==1):
    print("HARD")
else:
    print("easy")
