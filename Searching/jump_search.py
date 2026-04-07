"""
Jump Search

Requires the array to be sorted.

Time Complexity:
    Best:    O(1)
    Average: O(√n)
    Worst:   O(√n)
Space Complexity: O(1)
"""

import math


def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i

    return -1


if __name__ == "__main__":
    data = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
    target = 55
    result = jump_search(data, target)
    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found")
