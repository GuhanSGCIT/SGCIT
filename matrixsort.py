m,n=map(int,input().split())
lst=[]
a=[]
for i in range(m):
    lst.append(input().split())
for i in  lst:
    for j in i:
        a.append(j)
a.sort()
l=0
try:
    for i in range(0,(m*n)+1,n):
        for j in range(i,i+m):
            print(a[j],end=" ")
        print()
except:
    pass

        
        
    
