def duplicates_deletion(): 
    array_len = int(input())
    sorted_list = [int(x) for x in input().split()]

    result = []
    seen = set()

    for num in sorted_list:
        if num not in seen:
            result.append(num)
            seen.add(num)

    while len(result) < array_len:
        result.append("_")

    print(" ".join(map(str, result)))


duplicates_deletion()
