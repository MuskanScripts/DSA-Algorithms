"""
Longest Increasing Subsequence (LIS) — Dynamic Programming

Find the length of the longest strictly increasing subsequence
in an array.

Approach 1 — O(n^2) DP
Approach 2 — O(n log n) patience sorting with binary search
"""

import bisect


def lis_dp(arr):
    """O(n^2) DP approach."""
    if not arr:
        return 0
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def lis_binary_search(arr):
    """O(n log n) approach using binary search (patience sorting)."""
    tails = []
    for num in arr:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num
    return len(tails)


if __name__ == "__main__":
    data = [10, 9, 2, 5, 3, 7, 101, 18]
    print(f"Array: {data}")
    print(f"LIS length (O(n^2) DP):          {lis_dp(data)}")
    print(f"LIS length (O(n log n) bin search): {lis_binary_search(data)}")
