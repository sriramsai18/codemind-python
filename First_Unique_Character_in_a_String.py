s=input()
c=co=ind=0
for i in range(len(s)):
    c=0
    for j in range(len(s)):
        if i!=j:
            if s[i]==s[j]:
                c+=1
    if c!=0:
        continue
    else:
        ind=i
        co+=1
        break
if(co==0):
    print(-1)
else:
    print(ind)