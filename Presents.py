n=int(input())
s=input().split()
dic={}
for i in range(1,n+1):
    dic[i]= int(s[i-1])
c=1
while(c<n+1):
    for i in dic.keys():
        if (dic[i]==c):
            print(i,end=" ")
            c+=1
