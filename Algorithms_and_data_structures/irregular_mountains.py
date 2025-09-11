from array import array


def valid_mountain_array(heights: array) -> bool: 
    n = len(heights)
    if n < 3:
        return False

    max_height = max(heights)
    peak_index = heights.index(max_height)

    if peak_index == 0 or peak_index == n - 1:
        return False

    for index in range(peak_index):
        if heights[index] >= heights[index + 1]:
            return False

    for index in range(peak_index, n - 1):
        if heights[index] <= heights[index + 1]:
            return False

    return True 


heights = array('b', map(int, input().split()))
print(valid_mountain_array(heights))