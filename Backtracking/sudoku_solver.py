"""
Sudoku Solver — Backtracking

Solve a 9×9 Sudoku puzzle. Empty cells are represented by 0.

Rules:
- Each row must contain digits 1-9 without repetition.
- Each column must contain digits 1-9 without repetition.
- Each of the nine 3×3 sub-boxes must contain digits 1-9.

Time Complexity:  O(9^(n)) where n = number of empty cells
Space Complexity: O(n) recursion stack
"""


def is_valid(board, row, col, num):
    # Check row
    if num in board[row]:
        return False
    # Check column
    if num in (board[r][col] for r in range(9)):
        return False
    # Check 3x3 box
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if board[r][c] == num:
                return False
    return True


def solve_sudoku(board):
    """Solves in-place. Returns True if solvable, False otherwise."""
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def print_board(board):
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("------+-------+------")
        line = ""
        for j, val in enumerate(row):
            if j % 3 == 0 and j != 0:
                line += " | "
            line += str(val) if val != 0 else "."
            if j < 8:
                line += " "
        print(line)


if __name__ == "__main__":
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]
    print("Unsolved:")
    print_board(board)
    if solve_sudoku(board):
        print("\nSolved:")
        print_board(board)
    else:
        print("No solution exists.")
