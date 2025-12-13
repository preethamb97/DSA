"""
Binary Search - Fundamental Searching Algorithm
Frequency: 90% (Extremely common)

Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List, Optional


def binary_search(nums: List[int], target: int) -> int:
    """
    Standard binary search - returns index or -1
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def search_insert_position(nums: List[int], target: int) -> int:
    """
    Search Insert Position - LeetCode #35
    Return the index where target should be inserted
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left


def search_rotated_array(nums: List[int], target: int) -> int:
    """
    Search in Rotated Sorted Array - LeetCode #33
    Array is rotated at some pivot point
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1


def find_first_last_position(nums: List[int], target: int) -> List[int]:
    """
    Find First and Last Position - LeetCode #34
    Find starting and ending position of target in sorted array
    """
    def find_bound(is_first: bool) -> int:
        left, right = 0, len(nums) - 1
        bound = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                bound = mid
                if is_first:
                    right = mid - 1  # Continue searching left
                else:
                    left = mid + 1   # Continue searching right
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return bound
    
    first = find_bound(True)
    if first == -1:
        return [-1, -1]
    
    last = find_bound(False)
    return [first, last]


# Test cases
if __name__ == "__main__":
    # Standard binary search
    nums1 = [1, 3, 5, 7, 9, 11, 13]
    print(f"Search 7 in {nums1}: index {binary_search(nums1, 7)}")
    
    # Search insert position
    nums2 = [1, 3, 5, 6]
    print(f"Insert 5 in {nums2}: index {search_insert_position(nums2, 5)}")
    print(f"Insert 2 in {nums2}: index {search_insert_position(nums2, 2)}")
    
    # Rotated array
    nums3 = [4, 5, 6, 7, 0, 1, 2]
    print(f"Search 0 in rotated {nums3}: index {search_rotated_array(nums3, 0)}")
    
    # First and last position
    nums4 = [5, 7, 7, 8, 8, 10]
    print(f"Find 8 in {nums4}: {find_first_last_position(nums4, 8)}")

