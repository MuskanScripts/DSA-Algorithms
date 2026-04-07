"""
Interpolation Search

Requires a sorted array with uniformly distributed values.

Time Complexity:
    Best:    O(1)
    Average: O(log log n) — uniformly distributed data
    Worst:   O(n)
Space Complexity: O(1)
"""


def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1

        # Estimate the position using interpolation formula
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1


if __name__ == "__main__":
    data = [10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47]
    target = 18
    result = interpolation_search(data, target)
    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found")
