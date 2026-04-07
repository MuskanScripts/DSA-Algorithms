"""
Edit Distance (Levenshtein Distance) — Dynamic Programming

Find the minimum number of single-character edits (insertions,
deletions, or substitutions) required to convert one string
into another.

Time Complexity:  O(m * n)
Space Complexity: O(m * n) — can be reduced to O(min(m, n))
"""


def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # deletion
                    dp[i][j - 1],      # insertion
                    dp[i - 1][j - 1],  # substitution
                )

    return dp[m][n]


def edit_distance_optimized(s1, s2):
    """Space-optimized O(min(m,n)) version."""
    if len(s1) < len(s2):
        s1, s2 = s2, s1
    m, n = len(s1), len(s2)
    prev = list(range(n + 1))

    for i in range(1, m + 1):
        curr = [i] + [0] * n
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])
        prev = curr

    return prev[n]


if __name__ == "__main__":
    pairs = [("kitten", "sitting"), ("sunday", "saturday"), ("", "abc")]
    for s1, s2 in pairs:
        dist = edit_distance(s1, s2)
        print(f"Edit distance('{s1}', '{s2}') = {dist}")
