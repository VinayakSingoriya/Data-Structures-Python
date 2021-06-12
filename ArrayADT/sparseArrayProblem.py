# Problem: There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs  in the list of input strings. Return an array of the results.

def matchingStrings(strings, queries):
    result = list()
    for q in queries:
        count = 0
        for s in strings:
            if q == s:
                count += 1
        result.append(count)
    return result


if __name__ == '__main__':

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)
    print(*res, sep=" ")
