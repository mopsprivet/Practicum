def define_index(data_array, target_value): 
    min_index = 0
    max_index = len(data_array) - 1
    result = -1

    while min_index <= max_index:
        mid_index = (min_index + max_index) // 2

        if data_array[mid_index] == target_value:
            result = mid_index
            max_index = mid_index - 1
        elif data_array[mid_index] < target_value:
            min_index = mid_index + 1
        elif data_array[mid_index] > target_value:
            max_index = mid_index - 1

    if result != -1:
        return result  # вернём первый найденный индекс
    else:
        return min_index  # потому что мин индекс всегда является минимальным
# индексом, то есть местом, куда нужно вставить минимальное число, если его
# нет в массиве


data_array = list(map(int, input().split()))
target_value = int(input())

print(define_index(data_array, target_value))