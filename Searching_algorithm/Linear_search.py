# Python3 code to linearly search x in arr[].
# If x is present then return its location,
# otherwise return -1

def linearSearch(arr, x):  # Time complexity : O(n)
    for i in range(0, len(arr)):
        if arr[i] == x:
            return i
    return -1


arr = [25, 27, 2, 45, 67, 4]
x = 50

result = linearSearch(arr, x)
if(result == -1):
    print("Element not found")
else:
    print(f"Element found at index {result}")
