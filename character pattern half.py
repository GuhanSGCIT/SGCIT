n=int(input())
for i in range(n):
    for j in range(i):
        print("b",end="")
    for k in range(n-i):
        print("*",end="")
    print()
