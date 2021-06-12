   
def dynamicArray(n, queries):
    sequences = [[] for x in range(n)]
    answer = []
    lastAnswer = 0
    for query in queries:
        action, i, v = list(map(int, query))
        idx = (i^lastAnswer)%n
        if action == 1:
            sequences[idx].append(v)
        else:
            temp = sequences[idx]
            lastAnswer = sequences[idx][v%len(temp)]
            answer.append(lastAnswer)
    return answer 

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)
    for ans in result:
        print(ans)
        

