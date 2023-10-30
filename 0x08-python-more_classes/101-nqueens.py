#!/usr/bin/python3
"""a nqueen module"""
import sys


def is_safe(board, row, col, n):
    """Check if there is a queen in the same column"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def print_solution(board):
    """a the solution on the board"""
    n = len(board)
    for row in range(n):
        print("[{}, {}]".format(row, board[row]), end=" ")
    print()


def solve_nqueens(board, row, n):
    """solve the nqueen tasks"""
    if row == n:
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(board, row + 1, n)


def nqueens(n):
    """check is it is an integer"""
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)

    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve_nqueens(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
