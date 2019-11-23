n=int(input())
p=[int(o) for o in input().split()]
count=0
for i in range(n-1):
  if p[i]<p[i+1]:
    count+=1
print(count)
