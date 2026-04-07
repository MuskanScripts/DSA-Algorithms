"""
Counting Sort

Time Complexity:
    Best:    O(n + k)  where k is the range of input values
    Average: O(n + k)
    Worst:   O(n + k)
Space Complexity: O(k)

Note: Works only for non-negative integers.
"""


def counting_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    sorted_arr = []
    for i, c in enumerate(count):
        sorted_arr.extend([i] * c)

    return sorted_arr


if __name__ == "__main__":
    data = [4, 2, 2, 8, 3, 3, 1]
    print("Original:", data)
    print("Sorted:  ", counting_sort(data))
