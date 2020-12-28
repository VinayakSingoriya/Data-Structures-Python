def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while (i <= j):
    
        while((arr[i] < pivot) and (i < high)):
            i = i+1
        while(arr[j] > pivot):
            j = j-1
        if(i < j):
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i = i+1

    arr[low], arr[j] =  arr[j], arr[low]
    return j       



def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr,low, pi-1 )    
        quickSort(arr, pi+1, high)        

def printArray(arr):
    for element in arr:
        print(element, end = " ")




# Driver code
# arr = [1,2,3,9,4,4,8,7,5,6]
# arr = [48,44,19,59,72,80,42,65,82,8,95,68]
arr = [78,42,27,84,3,5]
n = len(arr)
print("Before sorting: ")
printArray(arr)
quickSort(arr, 0, n-1)
print("\nAfter sorting: ")
printArray(arr)

