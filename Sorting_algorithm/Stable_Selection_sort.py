# Program to implement Stable selection sort algorithm

def selection_sort(arr):
    # Traverse throgh all array elements
    for i in range(len(arr)):
        # Find the minimum element in a remaining unsorted array
        min_index = i
        for j in range(i+1, len(arr)):
            if (arr[min_index] > arr[j]):
                min_index = j

        # Move minimum element in current i
        key = arr[min_index] 
        while min_index > i:
            arr[min_index] = arr[min_index - 1]
            min_index -= 1
        arr[i] = key            

def printArray(arr):
    for i in arr:
        print(i, end = " ")

arr = [4,5,3,2,4,1]
selection_sort(arr)
printArray(arr)        