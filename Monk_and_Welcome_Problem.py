n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
for i in range(n):
    sum = 0
    for j in range(n):
        if i==j:
            sum += a[i]+b[j]
    print(sum,end=" ")