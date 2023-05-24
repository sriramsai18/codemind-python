a,b=map(int,input().split())
a=str(a)
s1=a[0:b]
s2=a[-b:]
print(abs(int(s2)-int(s1)))