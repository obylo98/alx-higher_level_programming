#!/usr/bin/python3
# 101-nqueens.py
"""Solves the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
Example:
    $ ./101-nqueens.py N
N must be an integer greater than or equal to 4.
Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.
Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys

def print_board(board):
    for row in board:
        print(row)

def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check diagonal top-left to bottom-right
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i] == j:
            return False
        i -= 1
        j -= 1

    # Check diagonal top-right to bottom-left
    i, j = row, col
    while i >= 0 and j < len(board):
        if board[i] == j:
            return False
        i -= 1
        j += 1

    return True

def solve(board, row):
    if row == len(board):
        print_board(board)
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            solve(board, row + 1)

def nqueens(n):
    if not n.isdigit() or int(n) < 4:
        print("N must be a number >= 4")
        return 1

    n = int(n)
    board = [-1] * n
    solve(board, 0)
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    sys.exit(nqueens(sys.argv[1]))
# End of 101-nqueens.py
