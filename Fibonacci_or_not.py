n=int(input())
j=0;a=0;b=1;
if (n==0) or (n==1):
    print("True")
else:
    c=a+b;
    while c<n:
        a=b
        b=c;
        c=a+b
if n==c:
    print("True")
else:
    print("False")