n=input().split()
m=input().split()
for i in m:
    if i in n:
    	n.pop(n.index(i))
print(*n)
