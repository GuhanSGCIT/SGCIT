n=int(input())
a = []
for i in range(2, n+1):
    if n%i==0:
        a.append(i)
l=[]
for i in a:
    if i % 2 == 0:
        l.append(i)
if len(l)>0:
    print(*l)
else:
    print(-1)
