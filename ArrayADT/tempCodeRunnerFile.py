def arrayManipulation(n, queries):
    arr = [0]*n
    for q in queries:
        start = q[0]
        end = q[1]
        val = q[2]
        for i in range(start, end+1):
            arr[i]+=val
    return arr        
    

if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    print(max(result))
