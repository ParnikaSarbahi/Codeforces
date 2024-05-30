'''
s=(input()).split()
n=int(s[0])
k=int(s[1])
if(n%2==0):
    if(k<=n//2):
        print(1+(k-1)*2)    
    else:
        print((k-n//2)*2)
else:
    if(k<=n//2+1):
        print(1+(k-1)*2)    
    else:
        print((k-(n//2)-1)*2)
'''
#better version
n, k = map(int, input().split()) #niceee
if k <= n-n//2:
    print(2*k-1)
else:
    k -= n-n//2
    print(2*k)
