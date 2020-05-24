def alternateSort(arr, n): 

	# Sorting the array 
	arr.sort() 

	# Printing the last element of array 
	# first and then first element and then 
	# second last element and then second 
	# element and so on. 
	i = 0
	j = n-1
	
	while (i < j): 
	
		print(arr[j], end =" ") 
		j-= 1
		print(arr[i], end =" ") 
		i+= 1

	# If the total element in array is odd 
	# then print the last middle element. 
	if (n % 2 != 0): 
		print(arr[i]) 


# Driver code 
n=int(input())
arr = [int(v) for v in input().split()] 
alternateSort(arr, n)
