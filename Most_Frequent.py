a = int(input())
x = list(map(int,input().split()))
y = set(x)
max = 0
for i in y:
    if x.count(i)>max:
        max=x.count(i)
        z = i
print(z)