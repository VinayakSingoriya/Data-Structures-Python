# Problem : A left rotation operation on an array of size n shifts each of the array's elements 1 unit to the left. Given an integer, d , rotate the array that many steps left and return the result.

def rotateLeft(d, arr):
    arr = arr[d:n]+arr[0:d]
    return arr


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = rotateLeft(d, arr)
    print(*result, sep=" ")
