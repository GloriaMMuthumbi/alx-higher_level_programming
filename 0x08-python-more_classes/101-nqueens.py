#!/usr/bin/python3
import sys


def is_safe(board, row, col, n):
    """
    Checks if it's safe to move queen to a give position on board

    Args:
        board (list): chessboard
        n (int): size of the board
        col (int): current column
        row (int): current row

    Returns:
        bool: True if it's safe, false if otherwise
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def print_solution(board):
    """
    Prints the current solution

    Args:
        board (list): chessboard
    """
    solution = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 1:
                solution.append([row, col])
    print(solution)


def solve_nqueens(board, col, n):
    """
    Solves the NQueens problem using backtracking

    Args:
        board (list): chessboard
        col (int): current column
        n (int): size of the board
    """
    if col == n:
        print_solution(board)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve_nqueens(board, col + 1, n)
            board[i][col] = 0


def nqueens(n):
    """
    Main function that solves the problem

    Args:
        n (str): size of the board

    Raises:
        SystemExit: if input is invalid
    """
    if not n.isdigit():
        print("N must be a number")
        sys.exit(1)
    n = int(n)
    if n < 4:
        print("N must be atleast 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_nqueens(board, 0, n)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    nqueens(sys.argv[1])
