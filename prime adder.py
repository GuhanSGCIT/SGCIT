i=1
x = int(input())
p=[]
p1=[]
counter = 0
while True:
    c=0;
    for j in range (1, (i+1), 1):
        a = i%j
        if (a==0):
            c = c+1
    if (c==2):
        p.append(i)
        counter = counter + 1
        if counter >= x:
            break
    i=i+1
sum=0
for i in range(x):
    sum+=p[i]
    p1.append(sum)
print(*p1)
