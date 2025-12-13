"""
Binary Tree Maximum Path Sum - LeetCode #124
Frequency: 75% (Very common)

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes 
has an edge connecting them. Find the maximum path sum.

Time Complexity: O(n)
Space Complexity: O(h) where h is height
"""

from typing import Optional
from .treeNode import TreeNode


def max_path_sum(root: Optional[TreeNode]) -> int:
    """
    DFS approach - track max path sum
    """
    max_sum = float('-inf')
    
    def dfs(node: Optional[TreeNode]) -> int:
        nonlocal max_sum
        
        if not node:
            return 0
        
        # Max path sum from left and right children
        left_sum = max(0, dfs(node.left))  # Ignore negative paths
        right_sum = max(0, dfs(node.right))
        
        # Current path sum (through current node)
        current_path = node.val + left_sum + right_sum
        
        # Update global max
        max_sum = max(max_sum, current_path)
        
        # Return max path sum that can be extended to parent
        return node.val + max(left_sum, right_sum)
    
    dfs(root)
    return max_sum


# Test cases
if __name__ == "__main__":
    # Tree: [-10, 9, 20, None, None, 15, 7]
    #        -10
    #        / \
    #       9   20
    #          /  \
    #         15   7
    root = TreeNode.from_list([-10, 9, 20, None, None, 15, 7])
    
    result = max_path_sum(root)
    print(f"Maximum path sum: {result}")  # Expected: 42 (15 + 20 + 7)

