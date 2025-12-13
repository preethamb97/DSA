"""
Binary Tree Traversals - Fundamental Tree Operations
"""

from typing import Optional, List
from .treeNode import TreeNode


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    Inorder: Left -> Root -> Right
    Time: O(n), Space: O(h) where h is height
    """
    result = []
    
    def inorder(node: Optional[TreeNode]):
        if node:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
    
    inorder(root)
    return result


def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    Preorder: Root -> Left -> Right
    """
    result = []
    
    def preorder(node: Optional[TreeNode]):
        if node:
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)
    
    preorder(root)
    return result


def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    Postorder: Left -> Right -> Root
    """
    result = []
    
    def postorder(node: Optional[TreeNode]):
        if node:
            postorder(node.left)
            postorder(node.right)
            result.append(node.val)
    
    postorder(root)
    return result


def level_order_traversal(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Level Order (BFS): Level by level from top to bottom
    """
    if not root:
        return []
    
    from collections import deque
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result


def inorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """
    Iterative inorder traversal using stack
    """
    result = []
    stack = []
    current = root
    
    while stack or current:
        # Go to leftmost node
        while current:
            stack.append(current)
            current = current.left
        
        # Process node
        current = stack.pop()
        result.append(current.val)
        
        # Move to right subtree
        current = current.right
    
    return result


# Test cases
if __name__ == "__main__":
    # Create tree: [1, 2, 3, 4, 5, None, 6]
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    root = TreeNode.from_list([1, 2, 3, 4, 5, None, 6])
    
    print("Inorder:", inorder_traversal(root))      # [4, 2, 5, 1, 3, 6]
    print("Preorder:", preorder_traversal(root))    # [1, 2, 4, 5, 3, 6]
    print("Postorder:", postorder_traversal(root))  # [4, 5, 2, 6, 3, 1]
    print("Level Order:", level_order_traversal(root))  # [[1], [2, 3], [4, 5, 6]]

