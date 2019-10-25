n=int(input())
l=[int(j) for j in input().split()]
m=l[::]
l.sort()
for i in l:
    print(m.index(i)+1,end=" ")
