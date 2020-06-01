n,m=map(int,input().split())
l=[int(b) for b in input().split()]
ll=[]
try:
    for i in range(n+1):
        if (l[i+1]-l[i])>15:
            ll.append(1)
        else:
            ll.append(0)
except:
    pass
print(*ll)
