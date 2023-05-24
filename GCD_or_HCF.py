a,b=map(int,input().split())
hcf=1
min=min(a,b)
for i in range(1,min+1):
    if a%i==0 and b%i==0:
        hcf=i
print(hcf)