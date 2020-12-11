#  Implemenation of Stable Bubble Sort Algorithm (Iterative).
# Time complexity => For unsorted = O(n^2), for sorted = O(n)
# Auxiliary space : O(1) 

def Bubblesort(arr, n):                     
    for i in range(0,n-1):
        # print(f"\n Working on pass number {i+1}") 
        isSorted = 1      
        for j in range(0, n-i-1):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                isSorted = 0

        if(isSorted):
            return        


def printArray(arr, n):  # Time complexity : O(n)
    for i in range(n):
        print(arr[i], end=" ")


# Driver mode
arr = [12, 54, 65, 7, 23, 9]       # Unsorted array
# arr = [1,2,3,4,5]                # Sorted array
n = len(arr)
print("Before sorting:")
printArray(arr, n)
Bubblesort(arr, n)
print("\n After sorting: ")
printArray(arr, n)
