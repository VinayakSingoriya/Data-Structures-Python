
from math import ceil
n = int(input())
arr = [int(i) for i in input().split() ]
for i in range(0, ceil(n/2)):
    arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
print(*arr, sep =" ")  
    