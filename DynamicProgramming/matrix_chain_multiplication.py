"""
Matrix Chain Multiplication — Dynamic Programming

Find the optimal parenthesization of a chain of matrices to
minimize the number of scalar multiplications needed.

Given a chain of matrices A1, A2, ..., An where Ai has
dimensions p[i-1] x p[i], find the minimum cost.

Time Complexity:  O(n^3)
Space Complexity: O(n^2)
"""


def matrix_chain_order(p):
    """
    p: list of dimensions where matrix i has size p[i-1] x p[i]
    Returns: minimum number of multiplications needed
    """
    n = len(p) - 1  # number of matrices
    # dp[i][j] = min cost to multiply matrices i through j (1-indexed)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for chain_len in range(2, n + 1):
        for i in range(1, n - chain_len + 2):
            j = i + chain_len - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[1][n]


if __name__ == "__main__":
    # Example: three matrices of sizes 40x20, 20x30, 30x10
    dims = [40, 20, 30, 10]
    print(f"Matrix dimensions: {dims}")
    print(f"Minimum multiplications: {matrix_chain_order(dims)}")

    # Another example: 4 matrices
    dims2 = [10, 30, 5, 60]
    print(f"\nMatrix dimensions: {dims2}")
    print(f"Minimum multiplications: {matrix_chain_order(dims2)}")
