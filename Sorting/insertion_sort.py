"""
Insertion Sort

Time Complexity:
    Best:    O(n)   — already sorted
    Average: O(n^2)
    Worst:   O(n^2)
Space Complexity: O(1)
"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    data = [12, 11, 13, 5, 6]
    print("Original:", data)
    print("Sorted:  ", insertion_sort(data))
