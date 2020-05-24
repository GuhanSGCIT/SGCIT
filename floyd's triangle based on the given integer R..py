def contnum(n): 
    num = 1
    for i in range(1, n+1):
        l=[]
        for j in range(i):
            l.append(num) 
            num = num + 1
        print(*l) 
n = int(input())
contnum(n) 
