# Given Problem statement:
# Given a 6*6 2D Array, :
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# We define an hourglass in A to be a subset of values with indices falling in this pattern in arr's graphical
# representation:
# a b c
# d
# e f g
# There are 16 hourglasses in arr, and an hourglass sum is the sum of an hourglass' values. Calculate the
# hourglass sum for every hourglass in arr, then print the maximum hourglass sum.



def hourglassSum(arr):
    resultList = []
    sum = None
    for i in range(4):
        for j in range(4):
            sum = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1] + \
                arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            resultList.append(sum)
    maxsum = max(resultList)
    return maxsum


if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)
