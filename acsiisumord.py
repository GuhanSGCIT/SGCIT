s=input()
lst=['a','e','o','i','u']
sum=0
for i in s:
    if i in lst:
        sum+=ord(i)

if sum%8==0:
    print(1)
else:
    print(0)
