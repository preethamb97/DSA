"""
Jump Game - LeetCode #55
Frequency: 75% (Very common)

You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


def can_jump(nums: List[int]) -> bool:
    """
    Greedy approach - track maximum reachable index
    """
    max_reach = 0
    
    for i in range(len(nums)):
        # If current index is beyond max reach, can't proceed
        if i > max_reach:
            return False
        
        # Update max reach
        max_reach = max(max_reach, i + nums[i])
        
        # Early exit if we can reach the end
        if max_reach >= len(nums) - 1:
            return True
    
    return True


def jump_game_ii(nums: List[int]) -> int:
    """
    Jump Game II - LeetCode #45
    Return the minimum number of jumps to reach the last index
    """
    if len(nums) <= 1:
        return 0
    
    jumps = 0
    current_end = 0
    farthest = 0
    
    for i in range(len(nums) - 1):
        # Update farthest reachable index
        farthest = max(farthest, i + nums[i])
        
        # If we've reached the end of current jump
        if i == current_end:
            jumps += 1
            current_end = farthest
            
            # Early exit
            if current_end >= len(nums) - 1:
                break
    
    return jumps


# Test cases
if __name__ == "__main__":
    # Test Jump Game
    test_cases = [
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
        ([0], True),
        ([2, 0, 0], True),
    ]
    
    print("=== Jump Game ===")
    for nums, expected in test_cases:
        result = can_jump(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} {nums} -> {result} (Expected: {expected})")
    
    # Test Jump Game II
    print("\n=== Jump Game II ===")
    nums = [2, 3, 1, 1, 4]
    result = jump_game_ii(nums)
    print(f"Minimum jumps for {nums}: {result}")  # Expected: 2

