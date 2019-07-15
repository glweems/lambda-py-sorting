arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# Try 1


def selection_sort(arr):
    # looper
    for i in range(0, len(arr) - 1):
        smallest_index = i
        for range_i in range(i, len(arr)):
            if arr[smallest_index] > arr[range_i]:
                smallest_index = range_i
            # The Switcha-roo
            arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


print(selection_sort(arr1))
