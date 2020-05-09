n=int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()
for k in range(1,n):
    for m in range(n-k):
        print("*",end="")
    print()
