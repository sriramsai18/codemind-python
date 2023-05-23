n = int(input())
a = list(map(int,input().split()))
c2 = 0
for i in a:
    c = 0
    temp = i
    while(temp):
        r = i%10
        c += 1
        temp = temp//10
    if c%2==0:
        c2 += 1
print(c2)