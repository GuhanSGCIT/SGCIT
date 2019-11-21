n=int(input())
k=[int(m) for m in input().split()]
sum=0
for i in range(n):
    o=k[i]
    for j in range(i+1,n):
        o+=k[j]
    print(o,end=" ")
