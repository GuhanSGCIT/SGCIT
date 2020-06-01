    n=int(input())
    ll=[]
    l=[int(v) for v in input().split()]
    for i,j in zip(range(n),l):
        if i==j:
            ll.append(j)
    ll.sort()
    if len(ll)>0:
        print(*ll)
    else:
        print(-1)
