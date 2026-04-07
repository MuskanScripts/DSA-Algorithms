"""
Exponential Search

Requires the array to be sorted. Works well when the target
is near the beginning of the array.

Time Complexity:
    Best:    O(1)
    Average: O(log n)
    Worst:   O(log n)
Space Complexity: O(1)
"""


def binary_search(arr, low, high, target):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def exponential_search(arr, target):
    n = len(arr)
    if n == 0:
        return -1
    if arr[0] == target:
        return 0

    # Find the range where target may exist
    i = 1
    while i < n and arr[i] <= target:
        i *= 2

    return binary_search(arr, i // 2, min(i, n - 1), target)


if __name__ == "__main__":
    data = [2, 3, 4, 10, 40, 55, 60, 80]
    target = 10
    result = exponential_search(data, target)
    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found")
