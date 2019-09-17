l=int(input())
a=str(l)
b=[]
for i in a:
    if i not in b:
        b.append(i)
if len(b)==2:
    print("Saturated")
else:
    print("Unsaturated")
