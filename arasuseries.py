n=int(input())
p=[]
l=1
for i in range(1,100,2):
    p.append(i)
for i in range(1,n+1):
    print(l+p[i-1],end=" ")
    l=l+p[i-1]
    
