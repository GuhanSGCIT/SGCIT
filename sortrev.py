# Python 3 program to sort first 
# k elements in increasing order 
# and remaining n-k elements in 
# decreasing 

# Function to sort the array 
def printOrder(arr, n, k): 

    len1 = k 
    len2 = n - k 
    arr1 = [0] * k 
    arr2 = [0] * (n - k) 
    for i in range(k): 
    	arr1[i] = arr[i] 
    for i in range(k, n): 
    	arr2[i - k] = arr[i] 
    arr1.sort()
    arr2.sort()
    for i in range(n): 
        if (i < k): 
            arr[i] = arr1[i]
        else:
            arr[i] = arr2[len2 - 1]
            len2 -= 1
    print(*arr,end="")
if __name__ == "__main__": 
    n,k=input().split()
    n=int(n)
    k=int()
    a=input()
    arr=a.split()
    if(len(arr)==n):
        printOrder(arr, n, k) 

