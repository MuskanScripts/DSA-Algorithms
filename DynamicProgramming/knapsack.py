"""
0/1 Knapsack Problem — Dynamic Programming

Given n items each with a weight and value, and a knapsack
with maximum capacity W, find the maximum value that can be
placed in the knapsack.

Time Complexity:  O(n * W)
Space Complexity: O(n * W)  — can be reduced to O(W)
"""


def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't include item i
            dp[i][w] = dp[i - 1][w]
            # Include item i if it fits
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])

    return dp[n][capacity]


def knapsack_optimized(weights, values, capacity):
    """Space-optimized version using a 1D DP array."""
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    return dp[capacity]


if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50

    print(f"Items:    values={values}, weights={weights}")
    print(f"Capacity: {capacity}")
    print(f"Max value (DP table):     {knapsack(weights, values, capacity)}")
    print(f"Max value (optimized DP): {knapsack_optimized(weights, values, capacity)}")
