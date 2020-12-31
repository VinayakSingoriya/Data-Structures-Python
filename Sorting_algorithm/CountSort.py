#Implementation of counting sort algorithm.

def countsSort(arr, n):
    # Initialize the count array to 0.
    count = [0 for i in range(max(arr)+1)]

    # Increment the corresponding index in the count array.
    for i in range(n):
        count[arr[i]] = count[arr[i]] + 1

    i = 0  # Counter for count array
    j = 0  # Counter for given array

    while(i < len(count)):
        if count[i] > 0:
            arr[j] = i
            count[i] -= 1
            j += 1
        else:
            i += 1

def printArray(arr):
    for i in arr:
        print(i, end=' ')

if __name__ == "__main__":
    # arr = [9, 1, 4, 14, 4, 15, 6]
    arr = [2, 1, 7, 4, 7, 22, 14]
    n = len(arr)
    print('Given Array :')
    printArray(arr)
    countsSort(arr, n)
    print("\nSorted array:")
    printArray(arr)
