n=int(input())
for i in range(1,n+1):
    k=0
    for j in range(i,n+1):
        k+=1
        print(f"{k}",end="")
    print()