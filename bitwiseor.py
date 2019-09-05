n = int(input())
array=[int(x) for x in input().split()]
result = 0
for i in range(len(array)-1):
  result=result|array[i]
print(result)  
