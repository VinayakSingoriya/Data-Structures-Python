# Program for recursive binary binarySearch

def binarySearch(arr, l, h, x):  # Time complexity : O(log n), Auxiliary space complexity : O(log n)
    if h >= l:
        mid = (l + h) // 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)

        # If element is greater than mid, then it
        # can only be present in right subarray
        else:
            return binarySearch(arr, mid+1, h, x)
    else:
        return -1


arr = [2, 3, 4, 10, 40]
x = 40
result = binarySearch(arr, 0, len(arr)-1, x)
if(result == -1):
    print("Element not found")
else:
    print(f"Element Found at index {result}")
