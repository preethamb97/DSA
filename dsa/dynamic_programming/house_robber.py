"""
House Robber - LeetCode #198
Frequency: 85% (Extremely common - Amazon favorite)

You are a robber planning to rob houses along a street. Each house has a certain amount of money stashed.
You cannot rob two adjacent houses. Determine the maximum amount of money you can rob.

Time Complexity: O(n)
Space Complexity: O(1) optimized
"""

from typing import List


def rob(nums: List[int]) -> int:
    """
    Space-optimized DP
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    prev2 = nums[0]
    prev1 = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        current = max(prev1, prev2 + nums[i])
        prev2, prev1 = prev1, current
    
    return prev1


def rob_circular(nums: List[int]) -> int:
    """
    House Robber II - LeetCode #213
    Houses are arranged in a circle (first and last are adjacent)
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    # Two cases: rob first house (exclude last) or rob last house (exclude first)
    return max(rob(nums[:-1]), rob(nums[1:]))


def rob_tree(root) -> int:
    """
    House Robber III - LeetCode #337
    Houses are arranged in a binary tree
    """
    def dfs(node):
        if not node:
            return (0, 0)  # (rob, not_rob)
        
        left = dfs(node.left)
        right = dfs(node.right)
        
        # If we rob this node, we cannot rob children
        rob = node.val + left[1] + right[1]
        
        # If we don't rob this node, we can choose to rob or not rob children
        not_rob = max(left) + max(right)
        
        return (rob, not_rob)
    
    return max(dfs(root))


# Test cases
if __name__ == "__main__":
    # Test House Robber
    nums1 = [2, 7, 9, 3, 1]
    print(f"Input: {nums1}")
    print(f"Maximum: {rob(nums1)}")  # Expected: 12 (2 + 9 + 1)
    
    # Test House Robber II (Circular)
    nums2 = [2, 3, 2]
    print(f"\nInput (circular): {nums2}")
    print(f"Maximum: {rob_circular(nums2)}")  # Expected: 3

