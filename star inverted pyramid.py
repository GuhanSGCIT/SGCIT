n=int(input())
for i in range(n):
    for j in range(n-i):
        if j==n-i:
            print("*")
        else:
            print("*",end=" ")
    print()
