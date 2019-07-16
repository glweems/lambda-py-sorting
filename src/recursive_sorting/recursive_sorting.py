
list1 = [100, 80, 90, 70, 60]
list2 = [10, 20, 30, 40, 50, 42]
list3 = [4, 9, 18, 1, 3, 22, 16, 19]


def pretty_print(arr):
    if len(arr) > 1:
        string = ''
        for i in arr:
            string = string + ' ' + str(i)
        print(string)

# Combine Two Lists


def merge(first, second):
    def get_yield(first, second):
        yield from first
        yield from second
    return list(get_yield(first, second))


def merge_sort(A):
    arr = A
    if len(arr) > 1:
         # Finding the mid of the array
        mid = len(arr)//2
        # Dividing the array elements
        L = arr[:mid]
        R = arr[mid:]

        # See what's happening
        pretty_print(L)
        pretty_print(R)

        # Sort each half
        merge_sort(L)
        merge_sort(R)

        # Set vars to 0
        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i = i+1
            else:
                arr[k] = R[j]
                j = j+1
            k = k+1

        while i < len(L):
            arr[k] = L[i]
            i = i+1
            k = k+1

        while j < len(R):
            arr[k] = R[j]
            j = j+1
            k = k+1

    return arr


print(merge_sort(merge(list1, merge(list2, list3))))


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr
