n=int(input())
ls=list(map(int,input().split()))
for i in ls:
    if i>=n:
        print("NO")
        break
else:
    print("YES")