def fact(r):
    f=1
    for i in range(1,r+1):
        f=f*i
    return f
n=int(input())
temp=n
s=0
while n>0:
    r=n%10
    s+=fact(r)
    n//=10
if s==temp:
    print("The number",temp,"is a strong number")
else:
    print("The number",temp,"is not a strong number")