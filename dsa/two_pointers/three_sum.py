"""
3Sum - LeetCode #15
Frequency: 90% (Extremely common)

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Time Complexity: O(n²)
Space Complexity: O(1) excluding output array
"""

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Sort + Two pointers approach
    """
    nums.sort()
    result: List[List[int]] = []
    n = len(nums)
    
    for i in range(n - 2):
        # Skip duplicates for first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left, right = i + 1, n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for left pointer
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for right pointer
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1
    
    return result


def three_sum_closest(nums: List[int], target: int) -> int:
    """
    Find three integers whose sum is closest to target
    """
    nums.sort()
    n = len(nums)
    closest_sum = float('inf')
    
    for i in range(n - 2):
        left, right = i + 1, n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return target
    
    return closest_sum


# Test cases
if __name__ == "__main__":
    # Test 3Sum
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = three_sum(nums1)
    print(f"Input: {nums1}")
    print(f"Result: {result1}")
    print(f"Expected: [[-1, -1, 2], [-1, 0, 1]]")
    
    # Test 3Sum Closest
    nums2 = [-1, 2, 1, -4]
    target = 1
    result2 = three_sum_closest(nums2, target)
    print(f"\n3Sum Closest - Input: {nums2}, Target: {target}")
    print(f"Result: {result2}")  # Expected: 2

