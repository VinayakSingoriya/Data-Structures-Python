# Implementation of insertion sort algorithm (Iterative).
# Time complexity : O(n^2)
# Best case complexity : O(n)
# Auxiliary space  : O(1)

def InsertionSort(arr, n):
    # Total number of passes: (n-1)
    for i in range(1, n):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position

        j = i-1

        while (j >= 0 and key < arr[j]):
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key


def printArray(arr, n):
    for i in arr:
        print(i, end=" ")


# Driver code:
arr = [7, 12, 3, 4, 1]
n = len(arr)
print("Before sorting : ")
printArray(arr, n)
print("\nAfter sorting : ")
InsertionSort(arr, n)
printArray(arr, n)
