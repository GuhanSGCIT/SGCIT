def getPairs(arr, n) : 
	
	# Set to store unique pairs 
	h = set() 
	for i in range(n - 1) : 
		for j in range(i + 1, n) : 
			
			# Create pair of (a[i], a[j]) 
			# and add it to the hashset 
			h.add((arr[i], arr[j])); 
			
	# Return the size of the HashSet 
	return len(h); 

# Driver code 
if __name__ == "__main__" : 
		
	 
	n = int(input()) 
	arr = [int(v) for v in input().split()]
	print(getPairs(arr, n)) 
	
