"""
Container With Most Water - LeetCode #11
Frequency: 95% (Universal question)

You are given an integer array height of length n. There are n vertical lines drawn such that 
the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def max_area(height: List[int]) -> int:
    """
    Two pointers approach
    """
    left, right = 0, len(height) - 1
    max_water = 0
    
    while left < right:
        # Calculate current area
        width = right - left
        current_area = width * min(height[left], height[right])
        max_water = max(max_water, current_area)
        
        # Move pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water


def max_area_brute_force(height: List[int]) -> int:
    """
    Brute force: O(n²) - for comparison
    """
    max_water = 0
    n = len(height)
    
    for i in range(n):
        for j in range(i + 1, n):
            width = j - i
            area = width * min(height[i], height[j])
            max_water = max(max_water, area)
    
    return max_water


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
    ]
    
    for height, expected in test_cases:
        result = max_area(height)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: {height} -> {result} (Expected: {expected})")

