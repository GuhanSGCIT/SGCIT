n = int(input())
l = [int(x) for x in input().split()]
sum = 0
ll=[]
for i in range(n):
    if l[i]%2==0:
        sum += l[i]
        ll.append(sum)
    else:
        #sum += l[i]
        ll.append(l[i])
print(*ll)
	
