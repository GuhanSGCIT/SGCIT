def pattern(n):
    for i in range(n):
        for j in range(i):
            print(' ',end="")
        l=[]
        for j in range(n-i):
            l.append('*')
        print(' '.join(l))
n=int(input())
pattern(n)
