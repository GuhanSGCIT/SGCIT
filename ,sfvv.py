n=int(input())
nn=input()
nnnn=''.join(sorted(nn))
for i in range(n):
    nnnn=nnnn.replace(nnnn[len(nnnn)-1],"")
print(nnnn)

