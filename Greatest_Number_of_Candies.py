x = int(input())
a = list(map(int,input().split()))
y = int(input())
for i in a:
    z = i+y
    if z>=max(a):
        print("True",end=" ")
    else:
        print("False",end=" ")