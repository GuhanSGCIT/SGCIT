(l, r, n) = map(int, input().split())
n = str(n)
count = 0
for i in range(l, r):
    if n in str(i):
        count += 1
#print(count)
