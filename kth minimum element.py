n=int(input())
def sam():
    m=int(input())
    l=[int(b) for b in input().split()]
    k=int(input())
    l=list(dict.fromkeys(l))
    for i in range(k):
        mi=min(l)
        l.pop(l.index(mi))
    return mi
for i in range(n):
    print(sam())
