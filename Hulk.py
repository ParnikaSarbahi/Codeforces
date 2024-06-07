n=int(input())
p=['I hate','I love']
if(n==1):
        print(p[0],"it")
else:
    for i in range(n):
        if(i%2==0):
            c=0
        else:
            c=1
        if(i!=n-1):
            print(p[c],end=" that ")
    print(p[c],"it")
  
#or
#print(*(['I hate','I love']*50)[:int(input())],sep=' that ',end=' it')
