n=int(input())
l=[int(v) for v in input().split()]
ll=[int(b) for b in input().split()]
k=[]
for i,j in zip(l,ll):
    k.append(i+j)
print(*k)
