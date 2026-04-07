"""
Binary Search

Requires the array to be sorted.

Time Complexity:
    Best:    O(1)
    Average: O(log n)
    Worst:   O(log n)
Space Complexity: O(1) iterative / O(log n) recursive
"""


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def binary_search_recursive(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


if __name__ == "__main__":
    data = [2, 3, 4, 10, 40]
    target = 10
    result = binary_search(data, target)
    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found")
