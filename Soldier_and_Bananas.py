s=input()
s1=s.split()
k=int(s1[0])
n=int(s1[1])
w=int(s1[2])
cost=0
for i in range(1,w+1):
    cost=cost+k*i
cost=cost-n
if(cost<=0):
    print(0)
else:
    print(cost)
