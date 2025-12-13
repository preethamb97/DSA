"""
Trapping Rain Water - LeetCode #42
Frequency: 85% (Extremely common)

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.

Time Complexity: O(n)
Space Complexity: O(1) optimized, O(n) with arrays
"""

from typing import List


def trap_two_pointers(height: List[int]) -> int:
    """
    Two pointers approach: O(n) time, O(1) space
    """
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water = 0
    
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    
    return water


def trap_stack(height: List[int]) -> int:
    """
    Stack approach: O(n) time, O(n) space
    """
    stack = []
    water = 0
    
    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            bottom = stack.pop()
            
            if not stack:
                break
            
            width = i - stack[-1] - 1
            trapped_height = min(height[i], height[stack[-1]]) - height[bottom]
            water += width * trapped_height
        
        stack.append(i)
    
    return water


def trap_dp(height: List[int]) -> int:
    """
    DP approach: O(n) time, O(n) space
    """
    if not height:
        return 0
    
    n = len(height)
    left_max = [0] * n
    right_max = [0] * n
    
    # Calculate max height from left
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], height[i])
    
    # Calculate max height from right
    right_max[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], height[i])
    
    # Calculate trapped water
    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - height[i]
    
    return water


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([], 0),
        ([1], 0),
    ]
    
    print("=== Trapping Rain Water ===")
    for height, expected in test_cases:
        result1 = trap_two_pointers(height)
        result2 = trap_stack(height)
        result3 = trap_dp(height)
        status = "✓" if result1 == expected else "✗"
        print(f"{status} {height}")
        print(f"  Two Pointers: {result1}, Stack: {result2}, DP: {result3} (Expected: {expected})")

