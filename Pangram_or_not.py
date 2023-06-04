s=input()
al="qwertyuiopasdfghjklmnbvcxz"
c=v=0
for i in al:
    if i in s or i.upper() in s:
        c+=1
    else:
        v=1
if v!=1:
    print(True)
else:
    print(False)