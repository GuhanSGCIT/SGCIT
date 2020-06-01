def maxOfSegmentMins(a,n,k): 

	# if we have to divide it into 1 segment 
	# then the min will be the answer 
	if k ==1: 
		return min(a) 
	if k==2: 
		return max(a[0],a[n-1]) 

	# If k >= 3, return maximum of all 
	# elements. 
	return max(a) 
	
# Driver code 
if __name__=='__main__': 
    n,k=map(int,input().split())
    a = [int(y) for y in input().split()] 
    print(maxOfSegmentMins(a,n,k)) 
