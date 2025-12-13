"""
Merge Sorted Array - LeetCode #88
Frequency: 85% (Extremely common)

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order.
Merge nums2 into nums1 as one sorted array.

Time Complexity: O(m + n)
Space Complexity: O(1)
"""

from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Merge from the end (in-place)
    """
    # Start from the end
    i = m - 1  # Last element in nums1
    j = n - 1  # Last element in nums2
    k = m + n - 1  # Last position in merged array
    
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    
    # Copy remaining elements from nums2
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1


# Test cases
if __name__ == "__main__":
    # Test case 1
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    
    merge(nums1, m, nums2, n)
    print(f"Merged: {nums1}")  # Expected: [1, 2, 2, 3, 5, 6]
    
    # Test case 2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    
    merge(nums1, m, nums2, n)
    print(f"Merged: {nums1}")  # Expected: [1]

