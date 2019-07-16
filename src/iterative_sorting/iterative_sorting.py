arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# Try 1


def selection_sort(arr):
    # Loop through array
    for i in range(len(arr)):
        # Find the minimum element in remaining unsorted array
        small_i = i
        for range_i in range(i, len(arr)):
            if arr[small_i] > arr[range_i]:
                small_i = range_i

        # Swap the found minimum element with the first element
        arr[i], arr[small_i] = arr[small_i], arr[i]

    # return that bitch
    return arr


print(selection_sort(arr1))
# Inital Array: [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# Sorted Array: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# What a bubble sorter this one was


def bubble_sort(lst):
    for i in range(len(lst)-1, 0, -1):
        for index in range(i):
            if lst[index] > lst[index + 1]:
                lst[index], lst[index + 1] = lst[index + 1], lst[index]
    return lst


print(bubble_sort(arr1))

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
