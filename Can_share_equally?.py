x,y=map(int,input().split())
n=x*1+y*2
if y%2!=0 and x==0:
    print("NO")
elif n%2==0:
    print("YES")
else:
    print("NO")