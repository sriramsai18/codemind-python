n = int(input())
a = list(map(int,input().split()))
sum1 = 0
sum2 = 0
for i in range(len(a)):
    if i%2==0:
        sum1 += a[i]
    if i%2!=0:
        sum2 += a[i]
if sum1==sum2:
    print("YES")
else:
    print("NO")