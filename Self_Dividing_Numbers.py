m=int(input())
n=int(input())
s=0
for i in range(m,n+1):
        c=0
        t=i
        while t:
            r=t%10
            if (r==0 or i%r!=0):
                c+=1
            t//=10
        if c==0:
            print(i,end=' ')