n,k=map(int,input().split())
lst=list(map(int,input().split()))
sum=0
o=0
for i in range(n):
    if i!=(n-1):
        f=lst[i]
        l=lst[i+1]
        sum=f+l
        if sum==k:
            o=1
    else:
        f=lst[i]
        l=lst[0]
        sum=f+l
        if sum==k:
            o=1
if o==1:
    print("yes")
else:
    print("no")
