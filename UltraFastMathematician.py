s=''
s1 = (input())
s2 = (input())
n=len(s2)
for i in range(n,0,-1):
	if s1[-i] == s2[-i]:
		s = s + '0'
	else:
		s = s + '1'
print(s)
