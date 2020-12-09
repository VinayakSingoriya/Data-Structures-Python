# Program for implementation of Selection_sort algorithm
arr = [25, 45, 34, 21, 6, 55]

for i in range(len(arr)):         #Time complexity : O(n^2)

    # Find the minimum element in a remaining unsorted array
    min_index = i
    for j in range(i+1, len(arr)):

        if(arr[min_index] > arr[j]):
            min_index = j

    # Swap the found minimum element with  
    # the first element 
    arr[i], arr[min_index] = arr[min_index], arr[i]

print("sorted array:", arr)
