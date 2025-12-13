"""
Permutations - LeetCode #46
Frequency: 75% (Very common)

Given an array nums of distinct integers, return all the possible permutations.

Time Complexity: O(n! * n)
Space Complexity: O(n! * n)
"""

from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    """
    Backtracking approach
    """
    result = []
    
    def backtrack(current: List[int], remaining: List[int]):
        # Base case: no more elements to choose
        if not remaining:
            result.append(current[:])  # Make a copy
            return
        
        # Try each remaining element
        for i in range(len(remaining)):
            # Choose
            current.append(remaining[i])
            new_remaining = remaining[:i] + remaining[i+1:]
            
            # Explore
            backtrack(current, new_remaining)
            
            # Unchoose (backtrack)
            current.pop()
    
    backtrack([], nums)
    return result


def permute_swap(nums: List[int]) -> List[List[int]]:
    """
    Backtracking with swapping (more space efficient)
    """
    result = []
    n = len(nums)
    
    def backtrack(first: int):
        if first == n:
            result.append(nums[:])
            return
        
        for i in range(first, n):
            # Swap
            nums[first], nums[i] = nums[i], nums[first]
            
            # Recurse
            backtrack(first + 1)
            
            # Backtrack (swap back)
            nums[first], nums[i] = nums[i], nums[first]
    
    backtrack(0)
    return result


def permute_unique(nums: List[int]) -> List[List[int]]:
    """
    Permutations II - LeetCode #47
    Handle duplicates
    """
    result = []
    nums.sort()  # Sort to handle duplicates
    
    def backtrack(current: List[int], used: List[bool]):
        if len(current) == len(nums):
            result.append(current[:])
            return
        
        for i in range(len(nums)):
            # Skip if already used
            if used[i]:
                continue
            
            # Skip duplicates (use first occurrence first)
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue
            
            # Choose
            used[i] = True
            current.append(nums[i])
            
            # Explore
            backtrack(current, used)
            
            # Unchoose
            current.pop()
            used[i] = False
    
    backtrack([], [False] * len(nums))
    return result


# Test cases
if __name__ == "__main__":
    # Test Permutations
    nums1 = [1, 2, 3]
    result1 = permute(nums1)
    print(f"Permutations of {nums1}:")
    for perm in result1:
        print(f"  {perm}")
    print(f"Total: {len(result1)} permutations")
    
    # Test Permutations with duplicates
    nums2 = [1, 1, 2]
    result2 = permute_unique(nums2)
    print(f"\nUnique permutations of {nums2}:")
    for perm in result2:
        print(f"  {perm}")
    print(f"Total: {len(result2)} unique permutations")

