n=input()
lst=[]
for i in n:
	lst.append(chr(ord(i)+3))
print(*lst,sep="")
