t=int(input())
for t in range(0,t):
    n,a,b,k=map(int,input().split())
    i=n/(a*b)
    u=n/a+n/b-i
    ans=u-i
    if ans>=k:
        print("Win")
    else:
        print("Lose")