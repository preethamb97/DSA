"""
Subsets - LeetCode #78
Frequency: 75% (Very common)

Given an integer array nums of unique elements, return all possible subsets (the power set).

Time Complexity: O(2^n * n)
Space Complexity: O(2^n * n)
"""

from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    """
    Backtracking approach
    """
    result = []
    
    def backtrack(start: int, current: List[int]):
        # Add current subset
        result.append(current[:])
        
        # Try each remaining element
        for i in range(start, len(nums)):
            # Choose
            current.append(nums[i])
            
            # Explore
            backtrack(i + 1, current)
            
            # Unchoose
            current.pop()
    
    backtrack(0, [])
    return result


def subsets_iterative(nums: List[int]) -> List[List[int]]:
    """
    Iterative approach using bit manipulation
    """
    result = []
    n = len(nums)
    
    # Each number from 0 to 2^n - 1 represents a subset
    for i in range(2 ** n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(nums[j])
        result.append(subset)
    
    return result


def subsets_with_dup(nums: List[int]) -> List[List[int]]:
    """
    Subsets II - LeetCode #90
    Handle duplicates
    """
    result = []
    nums.sort()  # Sort to handle duplicates
    
    def backtrack(start: int, current: List[int]):
        result.append(current[:])
        
        for i in range(start, len(nums)):
            # Skip duplicates (use first occurrence)
            if i > start and nums[i] == nums[i-1]:
                continue
            
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()
    
    backtrack(0, [])
    return result


# Test cases
if __name__ == "__main__":
    nums = [1, 2, 3]
    result = subsets(nums)
    print(f"Subsets of {nums}:")
    for subset in result:
        print(f"  {subset}")
    print(f"Total: {len(result)} subsets (2^{len(nums)} = {2**len(nums)})")

