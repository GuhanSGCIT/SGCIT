n,m=map(int,input().split())
for i in range(n):
    for j in range(m):
        if j==m-1:
            print("*")
        else:
            print("*",end=" ")
