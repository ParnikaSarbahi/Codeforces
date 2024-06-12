n = int(input())
y=[]
for i in range(n):
        a,b=map(int,input().split())
        c = 1
        if a % b == 0:
                y.append(0)
        else:
                y.append((b*(a//b+1))-a)
        
for i in y:
        print(i)
