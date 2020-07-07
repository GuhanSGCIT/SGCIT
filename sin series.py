import math
def sin(x,n):
    s = 0
    for i in range(n):
        sign = (-1)**i
        pi=22/7
        y=x*(pi/180)
        s = s + ((y**(2.0*i+1))/math.factorial(2*i+1))*sign
    return s
x=int(input("x in degrees: "))
n=int(input("number of terms "+"'n'" ": "))
print(round(sin(x,n),2))
