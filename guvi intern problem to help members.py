n=int(input())
import math
for i in range(n):
    m,k=map(int,input().split())
    print(int(pow(k,math.log(m)//math.log(k))))
    
    
    
