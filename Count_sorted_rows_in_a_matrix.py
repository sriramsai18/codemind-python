n,m=map(int,input().split())
co=0
for i in range(n):
    a=list(map(int,input().split()))
    b=a.copy()
    b.sort()
    c=b[::-1]
    if a==b or a==c:
        co+=1
print(co)