def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p - 1)
        quick_sort(arr, p + 1, high)


if __name__ == "__main__":
    test_lists = [
        [54, 26, 93, 17, 77, 31, 44, 55, 20],
        [1, 2, 3, 4, 5, 6],
        [4, 2, -3, 12, 4, 1, -5, 6, 0, 12]
    ]

    for idx, lst in enumerate(test_lists, 1):
        print(f"--- Test {idx} ---")
        print("Original:", lst)

        quick_sort(lst, 0, len(lst) - 1)

        print("Sorted:  ", lst)
