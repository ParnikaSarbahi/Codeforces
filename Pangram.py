n = int(input())
s = input().lower()
if n < 26:
    print("NO")
else:
    unique_chars = set(s)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    if alphabet.issubset(unique_chars):
        print("YES")
    else:
        print("NO")
