"""
Maximum Subarray - LeetCode #53
Frequency: 90% (Extremely common)

Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Time Complexity: O(n) Kadane's algorithm
Space Complexity: O(1)
"""

from typing import List


def max_subarray(nums: List[int]) -> int:
    """
    Kadane's algorithm: O(n) time, O(1) space
    """
    if not nums:
        return 0
    
    max_sum = nums[0]
    current_sum = nums[0]
    
    for i in range(1, len(nums)):
        # Either extend previous subarray or start new one
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum


def max_subarray_with_indices(nums: List[int]) -> tuple[int, int, int]:
    """
    Return (max_sum, start_index, end_index)
    """
    if not nums:
        return (0, -1, -1)
    
    max_sum = nums[0]
    current_sum = nums[0]
    start = 0
    end = 0
    temp_start = 0
    
    for i in range(1, len(nums)):
        if current_sum < 0:
            current_sum = nums[i]
            temp_start = i
        else:
            current_sum += nums[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    
    return (max_sum, start, end)


def max_subarray_circular(nums: List[int]) -> int:
    """
    Maximum Sum Circular Subarray - LeetCode #918
    Array is circular (can wrap around)
    """
    if not nums:
        return 0
    
    # Case 1: Maximum subarray is in middle (normal case)
    max_normal = max_subarray(nums)
    
    # Case 2: Maximum subarray wraps around
    # This equals total sum - minimum subarray
    total_sum = sum(nums)
    min_subarray = min_subarray_sum(nums)
    max_wrap = total_sum - min_subarray if min_subarray != total_sum else float('-inf')
    
    return max(max_normal, max_wrap)


def min_subarray_sum(nums: List[int]) -> int:
    """Find minimum subarray sum"""
    min_sum = nums[0]
    current_sum = nums[0]
    
    for i in range(1, len(nums)):
        current_sum = min(nums[i], current_sum + nums[i])
        min_sum = min(min_sum, current_sum)
    
    return min_sum


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
        ([-1], -1),
    ]
    
    print("=== Maximum Subarray ===")
    for nums, expected in test_cases:
        result = max_subarray(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} {nums} -> {result} (Expected: {expected})")
        
        # Get indices
        max_sum, start, end = max_subarray_with_indices(nums)
        print(f"  Subarray: {nums[start:end+1]} (indices {start}-{end})")
    
    # Test circular
    nums_circular = [5, -3, 5]
    result_circular = max_subarray_circular(nums_circular)
    print(f"\nCircular max subarray of {nums_circular}: {result_circular}")  # 10

