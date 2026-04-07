"""
Selection Sort

Time Complexity:
    Best:    O(n^2)
    Average: O(n^2)
    Worst:   O(n^2)
Space Complexity: O(1)
"""


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == "__main__":
    data = [64, 25, 12, 22, 11]
    print("Original:", data)
    print("Sorted:  ", selection_sort(data))
