n = int(input())
a = list(map(int,input().split()))
x = n//2
for i in range(n-1,(n//2)-1,-1):
    print(a[i],end=" ")
for i in range(n//2):
    print(a[i],end=" ")