n=input()
sum=0
for i in n:
    i=int(i)
    if i%2!=0:
        sum+=i
if sum%2==0:
    print("E")
else:
    print("O")
