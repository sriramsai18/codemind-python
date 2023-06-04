s=input()
v=0
for i in s:
    c=s.count(i)
    if c>1:
        print("False")
        v+=1
        break
if v==0:
    print("True")