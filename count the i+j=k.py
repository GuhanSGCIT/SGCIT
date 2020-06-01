def countTriplets(arr, n): 
	freq = [0 for i in range(100)] 
	
	# Loop to count the frequency 
	for i in range(n): 
		freq[arr[i]] += 1
	count = 0
	
	# Loop to count for triplets 
	for i in range(n): 
		for j in range(i + 1, n, 1): 
			if(freq[arr[i] + arr[j]]): 
				count += 1
	return count 

# Driver Code 
if __name__ == '__main__': 
	n = int(input())
	arr = [int(v) for v in input().split()] 
	
	# Function Call 
	print(countTriplets(arr, n)) 
