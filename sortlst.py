n=int(input())
lines = ""
for i in range(n):
    lines+=input()+"\n"
lst=lines.splitlines()
lst1=sorted(lst)
for i in lst1:
    print(i,end="\n")
