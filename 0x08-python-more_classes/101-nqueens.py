#!/usr/bin/python3
"""a nqueen module"""
import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at a specific position on the board.

    Args:
    - board (list): List representing the current state of the board.
    - row (int): Row index to check.
    - col (int): Column index to check.
    - n (int): Size of the board.

    Returns:
    - bool: True if it's safe, False otherwise.
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def print_solution(board):
    """
    Print the solution in the specified format.

    Args:
    - board (list): List representing the positions of queens on the board.
    """
    n = len(board)
    for row in range(n):
        print("[{}, {}]".format(row, board[row]), end=" ")
    print()


def solve_nqueens(board, row, n):
    """
    Recursively solve the N queens problem and print solutions.

    Args:
    - board (list): List representing the current state of the board.
    - row (int): Current row being considered.
    - n (int): Size of the board.
    """
    if row == n:
        print_solution(board)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row] = col
            solve_nqueens(board, row + 1, n)


def nqueens(n):
    """
    Main function to solve the N queens problem.

    Args:
    - n (str): Size of the chessboard.

    Prints:
    - All possible solutions to the N queens problem.
    """
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
