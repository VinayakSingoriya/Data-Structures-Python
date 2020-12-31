arr = [3,1,9,7,1,2,4]
count = [0 for i in range(max(arr)+1)]
for i in range(len(arr)):
    count[arr[i]] = count[arr[i]] + 1
print(count)    