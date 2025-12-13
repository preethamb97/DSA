"""
Invert Binary Tree - LeetCode #226
Frequency: 85% (Extremely common)

Given the root of a binary tree, invert the tree, and return its root.

Time Complexity: O(n)
Space Complexity: O(h) where h is height
"""

from typing import Optional
from .treeNode import TreeNode


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Recursive approach
    """
    if not root:
        return None
    
    # Swap left and right
    root.left, root.right = root.right, root.left
    
    # Recursively invert subtrees
    invert_tree(root.left)
    invert_tree(root.right)
    
    return root


def invert_tree_iterative(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    Iterative approach using queue (BFS)
    """
    if not root:
        return None
    
    from collections import deque
    
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        
        # Swap children
        node.left, node.right = node.right, node.left
        
        # Add children to queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return root


# Test cases
if __name__ == "__main__":
    # Original tree: [4, 2, 7, 1, 3, 6, 9]
    #       4
    #      / \
    #     2   7
    #    / \ / \
    #   1  3 6  9
    root = TreeNode.from_list([4, 2, 7, 1, 3, 6, 9])
    
    print("Original level order:", root.to_list())
    
    inverted = invert_tree(root)
    print("Inverted level order:", inverted.to_list() if inverted else [])
    # Expected: [4, 7, 2, 9, 6, 3, 1]

