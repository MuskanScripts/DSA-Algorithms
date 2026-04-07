"""
Longest Common Subsequence (LCS) — Dynamic Programming

Find the length of the longest subsequence common to two strings.
A subsequence preserves the relative order of characters but
does not need to be contiguous.

Time Complexity:  O(m * n)
Space Complexity: O(m * n)
"""


def lcs_length(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


def lcs_string(s1, s2):
    """Returns the actual LCS string."""
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack to find the LCS string
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcs.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(lcs))


if __name__ == "__main__":
    s1 = "ABCBDAB"
    s2 = "BDCAB"
    print(f"String 1: {s1}")
    print(f"String 2: {s2}")
    print(f"LCS length: {lcs_length(s1, s2)}")
    print(f"LCS string: {lcs_string(s1, s2)}")
