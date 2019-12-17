n=int(input())
l=[int(b) for b in input().split()]
m=[int(n) for n in input().split()]
sl=sorted(l)
for i,j in zip(l,sl):
    d=0
    if i!=j:
        d=l.index(i)-sl.index(j)
        print(d+1)
        m[l.index(i)]=m[l.index(i)]-(d+1)
print(m)
