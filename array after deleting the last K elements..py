n,m=map(int,input().split())
l=[int(o) for o in input().split()]
for j in range(m):
    l.pop(l.index(l[-1]))
print(*l)
