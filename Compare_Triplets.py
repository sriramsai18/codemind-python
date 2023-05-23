a = list(map(int,input().split()))
b = list(map(int,input().split()))
c1 = 0
c2 = 0
for i in range(len(a)):
    for i in range(len(b)):
        if a[i]<b[i]:
            c1 += 1
        if a[i]>b[i]:
            c2 += 1
    print(c2,c1)
    break