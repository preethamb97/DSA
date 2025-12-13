"""
N-Queens - LeetCode #51
Frequency: 70% (Common - Backtracking classic)

The n-queens puzzle is the problem of placing n queens on an n x n chessboard 
such that no two queens attack each other.

Time Complexity: O(n!)
Space Complexity: O(n)
"""

from typing import List


def solve_n_queens(n: int) -> List[List[str]]:
    """
    Backtracking approach
    """
    result = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    
    def is_safe(row: int, col: int) -> bool:
        """Check if placing queen at (row, col) is safe"""
        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check diagonal (top-left to bottom-right)
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        # Check diagonal (top-right to bottom-left)
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True
    
    def backtrack(row: int):
        if row == n:
            # Found a solution
            result.append([''.join(row) for row in board])
            return
        
        for col in range(n):
            if is_safe(row, col):
                # Place queen
                board[row][col] = 'Q'
                
                # Recurse
                backtrack(row + 1)
                
                # Backtrack
                board[row][col] = '.'
    
    backtrack(0)
    return result


def total_n_queens(n: int) -> int:
    """
    N-Queens II - LeetCode #52
    Return the number of distinct solutions
    """
    count = 0
    cols = set()
    diag1 = set()  # row - col
    diag2 = set()  # row + col
    
    def backtrack(row: int):
        nonlocal count
        
        if row == n:
            count += 1
            return
        
        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            
            # Place queen
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            
            # Recurse
            backtrack(row + 1)
            
            # Backtrack
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
    
    backtrack(0)
    return count


# Test cases
if __name__ == "__main__":
    n = 4
    solutions = solve_n_queens(n)
    print(f"Solutions for {n}-Queens:")
    for i, solution in enumerate(solutions, 1):
        print(f"\nSolution {i}:")
        for row in solution:
            print(f"  {row}")
    
    print(f"\nTotal solutions: {len(solutions)}")
    print(f"Total (optimized): {total_n_queens(n)}")

