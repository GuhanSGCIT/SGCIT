l="+-*/%"
ll=""
v=input()
for i in v:
    if i in l:
        print(i,end="")
    elif i.isalpha():
        ll=ll+i
print(ll)
