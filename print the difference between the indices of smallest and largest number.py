n = int(input())
l = [int(x) for x in input().split(" ")]
ma=max(l)
mi=min(l)
print(l.index(ma)-l.index(mi))
