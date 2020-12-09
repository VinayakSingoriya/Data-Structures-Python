# Program to implement Iterative Binary Search operation
def binarySearch(arr, l, h, x):  # Time complexity : O(log n)
    while h >= l:
        mid = (l+h)//2

        # Check if the target element is mid itself
        if (arr[mid] == x):
            return mid

        # If  x is greater than mid, then ignore left half
        elif (x > arr[mid]):
            l = mid + 1

        # If x is less than mid, then ignore right half
        else:
            h = mid - 1

            print("2:", l)

    return -1


arr = [34, 35, 36, 37, 38]
x = 34
result = binarySearch(arr, 0, len(arr)-1, x)
if(result == -1):
    print("Element not found.")
else:
    print(f"Element found at index {result}")
