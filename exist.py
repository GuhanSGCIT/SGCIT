n,k = input().split()
n = int(n)
k = int(k)
l=input()
lst=l.split()
for i in lst:
    if(k==i):
        m=1
        break
if(m==1):
    print("yes")
else:
    print("no")
