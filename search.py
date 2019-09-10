n,k=input().split()
n=int(n)
k=int(k)
lst=[int(i) for i in input().split()]
cout=0
if(n==len(lst)):
    lst.sort()
    if k in lst:
        print("yes")
    else:
        print("no")
