st=input()
st=list(st)
for i in range(0,len(st)):
    if(st[i]=='6'):
        st[i]='9'
        break
st="".join(st)
print(st)