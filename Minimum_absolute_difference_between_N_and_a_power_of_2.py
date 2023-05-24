import math
a=int(input())
arr=[]
for i in range(100):
    arr.append(math.pow(2,i))
f=l=df=dl=0
for i in range(100):
    if arr[i]>a:
        l=arr[i]
        f=arr[i-1]
        dl=l-a
        df=a-f
        print("{:.0f}".format(min(dl,df)))
        break