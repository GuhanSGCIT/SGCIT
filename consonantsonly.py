n=input()
lst=['a','A','e','E','i','I','o','O','u','U']
lst1=[]
for i in n:
    if i not in lst:
        lst1.append(i)
if lst1[0]==" ":
    lst1.pop(0)
print(*lst1,sep="")
