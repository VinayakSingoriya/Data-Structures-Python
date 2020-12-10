# Implementation of Stable Bubble Sort Algoritm (Recursive).
# Time complexity : O(n^2)

def recursiveBubbleSort(arr, n):
    
    isSorted = True
    #Base Case
    if n==1:
        return
    else:
        # One pass of bubble sort. After
        # this pass, the largest element
        # is moved (or bubbled) to end.
        for i in range(n-1):
            if(arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                isSorted = False

        if(isSorted):
            return        

        # Largest element is fixed, reccur for remaining array
        recursiveBubbleSort(arr, n-1)  

def printArray(arr,n):
    for i in range(n):
        print(arr[i], end = " ")

# Driver mode
arr = [64, 34, 25, 12, 22, 11, 90]       # Unsorted array
# arr = [3,4,5,6,7,8]                    #Sorted array
n = len(arr)
print("Before sorting : ")
printArray(arr, n)
recursiveBubbleSort(arr, n)
print("\n After sorting:")
printArray(arr, n)




