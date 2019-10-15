n=int(input())
lst=[int(l) for l in input().split()]
sum=0
for i in lst:
    if i>sum:
        sum+=1
if sum>0:
    print(sum)
else:
    print(-1)
