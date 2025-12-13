"""
Number of Islands - LeetCode #200
Frequency: 90% (Extremely common - Google favorite)

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

Time Complexity: O(m * n)
Space Complexity: O(m * n) worst case (DFS stack)
"""

from typing import List


def num_islands_dfs(grid: List[List[str]]) -> int:
    """
    DFS approach - mark visited islands
    """
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    def dfs(r: int, c: int):
        """Mark all connected land as visited"""
        if (r < 0 or r >= rows or c < 0 or c >= cols or 
            grid[r][c] != '1'):
            return
        
        # Mark as visited
        grid[r][c] = '0'
        
        # Explore all 4 directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)
    
    return count


def num_islands_bfs(grid: List[List[str]]) -> int:
    """
    BFS approach using queue
    """
    if not grid or not grid[0]:
        return 0
    
    from collections import deque
    
    rows, cols = len(grid), len(grid[0])
    count = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                count += 1
                queue = deque([(i, j)])
                grid[i][j] = '0'
                
                while queue:
                    r, c = queue.popleft()
                    
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (0 <= nr < rows and 0 <= nc < cols and 
                            grid[nr][nc] == '1'):
                            grid[nr][nc] = '0'
                            queue.append((nr, nc))
    
    return count


# Test cases
if __name__ == "__main__":
    grid1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    
    grid2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    
    # Note: grid is modified in-place, so we need to copy for second test
    import copy
    
    print(f"Grid 1 - Islands: {num_islands_dfs(copy.deepcopy(grid1))}")  # Expected: 1
    print(f"Grid 2 - Islands: {num_islands_dfs(copy.deepcopy(grid2))}")  # Expected: 3

