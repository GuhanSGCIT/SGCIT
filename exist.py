n,k = input().split()
n = int(n)
k = int(k)
lst=[int(y) for y in input().split()]
print(lst)
for i in lst:
    if(i==k):
        print("Yes")
        break
