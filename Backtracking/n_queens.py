"""
N-Queens Problem — Backtracking

Place N chess queens on an N×N board such that no two queens
attack each other (no two queens share the same row, column,
or diagonal).

Time Complexity:  O(N!)
Space Complexity: O(N)
"""


def solve_n_queens(n):
    """Returns all valid queen placements as lists of column positions per row."""
    solutions = []
    queens = []  # queens[i] = column of queen in row i

    def is_safe(row, col):
        for r, c in enumerate(queens):
            if c == col or abs(r - row) == abs(c - col):
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(queens[:])
            return
        for col in range(n):
            if is_safe(row, col):
                queens.append(col)
                backtrack(row + 1)
                queens.pop()

    backtrack(0)
    return solutions


def print_board(solution):
    n = len(solution)
    for col in solution:
        print("." * col + "Q" + "." * (n - col - 1))
    print()


if __name__ == "__main__":
    n = 8
    solutions = solve_n_queens(n)
    print(f"Number of solutions for {n}-Queens: {len(solutions)}")
    print(f"First solution (column positions per row): {solutions[0]}")
    print("First solution board:")
    print_board(solutions[0])
