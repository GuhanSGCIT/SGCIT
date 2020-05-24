def pat(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(' ',end="")
        l=[]
        if i ==1:
            l.appnd('*')
        elif i==n:
            for j in range(n):
                l.append('*')
        else:
            l.append('*')
            for j in range(i-2):
                l.append('*')
            l.append('*')
        print(*l)
n=int(input())
pat(n)
