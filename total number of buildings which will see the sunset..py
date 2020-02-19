def sunset(arr,n):
    count = 1
    arr=arr[::-1]
    curr_max = arr[0] 
    for i in range(1, n): 	
        if (arr[i] > curr_max): 
            count += 1
            curr_max = arr[i] 
    return count 
if __name__=="__main__":
    n=int(input())
    for i in range(n):
        m=int(input())
        l=[int(b) for b in input().split()]
        print(sunset(l,m))
