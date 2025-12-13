"""
Longest Increasing Subsequence - LeetCode #300
Frequency: 80% (Very common)

Given an integer array nums, return the length of the longest strictly increasing subsequence.

Time Complexity: O(n²) or O(n log n) with binary search
Space Complexity: O(n)
"""

from typing import List
import bisect


def length_of_lis_dp(nums: List[int]) -> int:
    """
    DP approach: O(n²) time
    """
    n = len(nums)
    dp = [1] * n  # dp[i] = length of LIS ending at index i
    
    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)


def length_of_lis_binary_search(nums: List[int]) -> int:
    """
    Binary search approach: O(n log n) time
    """
    tails = []  # tails[i] = smallest tail of all increasing subsequences of length i+1
    
    for num in nums:
        # Binary search for the position to insert/replace
        pos = bisect.bisect_left(tails, num)
        
        if pos == len(tails):
            # num is larger than all elements, extend
            tails.append(num)
        else:
            # Replace element at pos with smaller num
            tails[pos] = num
    
    return len(tails)


def find_number_of_lis(nums: List[int]) -> int:
    """
    Number of Longest Increasing Subsequence - LeetCode #673
    Return the number of longest increasing subsequences
    """
    n = len(nums)
    lengths = [1] * n  # Length of LIS ending at i
    counts = [1] * n   # Count of LIS ending at i
    
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                if lengths[j] + 1 > lengths[i]:
                    lengths[i] = lengths[j] + 1
                    counts[i] = counts[j]
                elif lengths[j] + 1 == lengths[i]:
                    counts[i] += counts[j]
    
    max_length = max(lengths)
    return sum(counts[i] for i in range(n) if lengths[i] == max_length)


# Test cases
if __name__ == "__main__":
    # Test LIS
    test_cases = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7, 7, 7], 1),
    ]
    
    print("=== Longest Increasing Subsequence ===")
    for nums, expected in test_cases:
        result1 = length_of_lis_dp(nums)
        result2 = length_of_lis_binary_search(nums)
        status = "✓" if result1 == expected else "✗"
        print(f"{status} {nums}")
        print(f"  DP: {result1}, Binary Search: {result2} (Expected: {expected})")
    
    # Test Number of LIS
    nums = [1, 3, 5, 4, 7]
    result = find_number_of_lis(nums)
    print(f"\nNumber of LIS for {nums}: {result}")  # Expected: 2

