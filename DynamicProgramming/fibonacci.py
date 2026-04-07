"""
Fibonacci Sequence — Dynamic Programming

Three approaches:
1. Recursive with memoization (top-down DP)
2. Bottom-up DP (tabulation)
3. Space-optimized bottom-up

Time Complexity: O(n)
Space Complexity:
    Memoization: O(n)
    Bottom-up:   O(n)
    Optimized:   O(1)
"""


def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


def fibonacci_dp(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def fibonacci_optimized(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    n = 10
    print(f"Fibonacci({n}) using memoization: {fibonacci_memo(n)}")
    print(f"Fibonacci({n}) using bottom-up DP: {fibonacci_dp(n)}")
    print(f"Fibonacci({n}) using optimized:    {fibonacci_optimized(n)}")
    print(f"First {n + 1} numbers:", [fibonacci_optimized(i) for i in range(n + 1)])
