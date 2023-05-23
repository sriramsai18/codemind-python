for _ in range(int(input())):
    x = int(input())
    temp = x
    j = []
    c = 0
    while(temp):
        r = temp%10
        j.append(r)
        temp//=10
    j = j[::-1]
    j.sort()
    for i in range(len(j)-1):
        if(j[i+1]-j[i]!=1):
            c += 1
    if c>0:
        print("NO")
    else:
        print("YES")