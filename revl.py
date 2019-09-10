n=int(input())
m=input()
lst=m.split()
lst1=lst[::-1]
print(lst1)
for i in lst1:
    if(lst1[len(lst1)-1]!=i):
        print(i+"->",end="")
print(lst1[len(lst1)-1])
        
