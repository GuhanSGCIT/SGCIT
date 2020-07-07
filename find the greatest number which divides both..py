n=list(map(int,input().split()))
m=min(n)
ans=0
for i in range(1,m+1):
    if n[0]%i==0 and n[1]%i==0:
        ans=i

print(ans)
