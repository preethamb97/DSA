"""
Unit tests for Two Sum problem
"""

import pytest
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from dsa.arrays_strings.two_sum import two_sum_optimal, two_sum_brute_force


class TestTwoSum:
    """Test cases for Two Sum"""
    
    def test_basic_case(self):
        """Test basic two sum case"""
        nums = [2, 7, 11, 15]
        target = 9
        result = two_sum_optimal(nums, target)
        assert result == [0, 1] or result == [1, 0]
    
    def test_no_solution(self):
        """Test case with no solution"""
        nums = [2, 7, 11, 15]
        target = 100
        result = two_sum_optimal(nums, target)
        assert result == []
    
    def test_duplicate_numbers(self):
        """Test with duplicate numbers"""
        nums = [3, 3]
        target = 6
        result = two_sum_optimal(nums, target)
        assert len(result) == 2
        assert nums[result[0]] + nums[result[1]] == target
    
    def test_negative_numbers(self):
        """Test with negative numbers"""
        nums = [-1, -2, -3, -4, -5]
        target = -8
        result = two_sum_optimal(nums, target)
        assert len(result) == 2
        assert nums[result[0]] + nums[result[1]] == target
    
    def test_single_element(self):
        """Test with single element"""
        nums = [1]
        target = 2
        result = two_sum_optimal(nums, target)
        assert result == []
    
    def test_brute_force_consistency(self):
        """Test that brute force and optimal give same results"""
        test_cases = [
            ([2, 7, 11, 15], 9),
            ([3, 2, 4], 6),
            ([3, 3], 6),
        ]
        
        for nums, target in test_cases:
            result_optimal = two_sum_optimal(nums, target)
            result_brute = two_sum_brute_force(nums, target)
            
            if result_optimal:
                assert nums[result_optimal[0]] + nums[result_optimal[1]] == target
            if result_brute:
                assert nums[result_brute[0]] + nums[result_brute[1]] == target


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

