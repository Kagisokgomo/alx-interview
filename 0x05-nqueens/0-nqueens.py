#!/usr/bin/python3

import sys

def print_solutions(solutions):
    for solution in solutions:
        print(solution)

def is_safe(board, row, col):
    # Check this column on upper side
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(board, row, solutions):
    if row == len(board):
        solutions.append([(i, board[i]) for i in range(len(board))])
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(board, row + 1, solutions)
            board[row] = -1  # backtrack

def nqueens(N):
    board = [-1] * N
    solutions = []
    solve_nqueens(board, 0, solutions)
    print_solutions(solutions)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N)


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at position (row, col) on the board.
    It checks the column and both diagonals.
    """
    for i in range(row):
        # Check the column
        if board[i][1] == col:
            return False
        # Check the diagonals
        if abs(board[i][1] - col) == abs(i - row):
            return False
    return True

def solve_nqueens(N):
    """
    Solve the N-Queens problem using backtracking.
    """
    def backtrack(board, row):
        if row == N:
            print(board)
            return
        
        for col in range(N):
            if is_safe(board, row, col, N):
                board.append([row, col])
                backtrack(board, row + 1)
                board.pop()  # Backtrack

    # Start solving with an empty board
    backtrack([], 0)

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N-Queens problem
    solve_nqueens(N)

if __name__ == "__main__":
    main()
