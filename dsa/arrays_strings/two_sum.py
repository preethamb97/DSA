"""
Two Sum - LeetCode #1
Frequency: 100% (Most asked question worldwide)

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List, Dict


def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    """
    Brute force approach: O(n²) time
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_optimal(nums: List[int], target: int) -> List[int]:
    """
    Optimal approach using hash map: O(n) time
    """
    num_map: Dict[int, int] = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    
    return []


def two_sum_sorted(nums: List[int], target: int) -> List[int]:
    """
    Two pointers approach for sorted array: O(n log n) time
    """
    # Create list of (value, original_index) pairs
    indexed_nums = [(nums[i], i) for i in range(len(nums))]
    indexed_nums.sort()
    
    left, right = 0, len(indexed_nums) - 1
    
    while left < right:
        current_sum = indexed_nums[left][0] + indexed_nums[right][0]
        
        if current_sum == target:
            return [indexed_nums[left][1], indexed_nums[right][1]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []


# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Input: {nums1}, Target: {target1}")
    print(f"Result: {two_sum_optimal(nums1, target1)}")  # Expected: [0, 1]
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"\nInput: {nums2}, Target: {target2}")
    print(f"Result: {two_sum_optimal(nums2, target2)}")  # Expected: [1, 2]
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    print(f"\nInput: {nums3}, Target: {target3}")
    print(f"Result: {two_sum_optimal(nums3, target3)}")  # Expected: [0, 1]

