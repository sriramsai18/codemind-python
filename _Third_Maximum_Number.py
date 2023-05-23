n = int(input())
a = list(map(int,input().split()))
a = set(a)
if len(a)==1:
    print(max(a))
elif len(a)==2:
    print(max(a))
elif len(a)==3:
    print(min(a))
else:
    a.remove(max(a))
    a.remove(max(a))
    print(max(a))