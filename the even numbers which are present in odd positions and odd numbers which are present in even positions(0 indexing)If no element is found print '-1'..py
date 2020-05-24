n=int(input())
list1 = [int(v) for v in input().split()] 
odd_list = []
even_list = []
for i in range(len(list1)):
    if((list1[i] % 2) == 0):
        even_list.append(list1[i])
    else:
        odd_list.append(list1[i])
#print(list1)
j = 0
k = 0
for i in range(0, len(list1)):
    if((i % 2 == 0) and (j < len(odd_list))):
        list1[i] = odd_list[j]
        j += 1
    elif(k < len(even_list)):
        list1[i] = even_list[k]
        k += 1
print(*list1)
