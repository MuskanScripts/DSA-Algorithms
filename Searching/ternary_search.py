"""
Ternary Search

Requires the array to be sorted. Divides the search space into
three parts instead of two (as in binary search).

Time Complexity:
    Best:    O(1)
    Average: O(log3 n)
    Worst:   O(log3 n)
Space Complexity: O(1) iterative / O(log3 n) recursive
"""


def ternary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        third = (high - low) // 3
        mid1 = low + third
        mid2 = high - third

        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        if target < arr[mid1]:
            high = mid1 - 1
        elif target > arr[mid2]:
            low = mid2 + 1
        else:
            low = mid1 + 1
            high = mid2 - 1

    return -1


if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    target = 11
    result = ternary_search(data, target)
    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found")
