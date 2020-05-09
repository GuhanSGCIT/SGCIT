n=int(input())
l=[int(b) for b in input().split()]
m=int(input())
ll=[]
for i in l:
    if i%m==0:
        ll.append(1)
    else:
        ll.append(0)
print(*ll)
