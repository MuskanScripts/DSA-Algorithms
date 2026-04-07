"""
Quick Sort

Time Complexity:
    Best:    O(n log n)
    Average: O(n log n)
    Worst:   O(n^2) — when pivot is smallest or largest element
Space Complexity: O(log n) average (recursive call stack)
"""


def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_idx = partition(arr, low, high)
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)
    return arr


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    print("Original:", data)
    print("Sorted:  ", quick_sort(data))
