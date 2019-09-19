n=input().split()
lst=[]
for i in n:
    if i.isdigit():
        lst.append(i)

print(max(lst))
