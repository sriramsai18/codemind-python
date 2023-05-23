a = int(input())
b = int(input())
sum = 0
for i in range(1,a+1):
    x = list(map(int,input().split()))
    for i in x:
        sum = sum+i
print(sum)