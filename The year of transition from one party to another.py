n=int(input())
l=[int(n) for n in input().split()]
dicti={}
p=[str(v) for v in input().split()]
for i,j in zip(l,p):
    dicti[i]=dicti.get(j)
print(dicti)
