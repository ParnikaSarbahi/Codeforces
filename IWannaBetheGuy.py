n = int(input())
a = {str(x) for x in range(1, n + 1)}
p=set(input().split()[1:])
q=set(input().split()[1:])
if(p.union(q)==a):
        print("I become the guy.")
else:
        print("Oh, my keyboard!")
