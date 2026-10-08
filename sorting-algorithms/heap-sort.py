def heapify(arr: list[int], n: int, i: int) -> None:
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr: list[int]) -> list[int]:
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap
        heapify(arr, i, 0)

    return arr


if __name__ == "__main__":
    test_lists = [
        [54, 26, 93, 17, 77, 31, 44, 55, 20],
        [1, 2, 3, 4, 5, 6],
        [4, 2, -3, 12, 4, 1, -5, 6, 0, 12]
    ]

    for idx, lst in enumerate(test_lists, 1):
        print(f"--- Test {idx} ---")
        print("Original:", lst)

        sorted_lst = heap_sort(lst.copy())

        print("Sorted list:  ", sorted_lst)
        