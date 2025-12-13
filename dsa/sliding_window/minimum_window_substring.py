"""
Minimum Window Substring - LeetCode #76
Frequency: 85% (Extremely common)

Given two strings s and t of lengths m and n respectively, 
return the minimum window substring of s such that every character in t 
(including duplicates) is included in the window.

Time Complexity: O(|s| + |t|)
Space Complexity: O(|s| + |t|)
"""

from typing import Dict
from collections import Counter


def min_window(s: str, t: str) -> str:
    """
    Sliding window with two pointers
    """
    if not s or not t or len(s) < len(t):
        return ""
    
    # Count characters in t
    required: Dict[str, int] = Counter(t)
    required_count = len(required)
    
    # Sliding window
    left = 0
    formed = 0
    window_counts: Dict[str, int] = {}
    
    # Result: (window length, left, right)
    result = (float('inf'), 0, 0)
    
    for right in range(len(s)):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        # Check if current character matches required count
        if char in required and window_counts[char] == required[char]:
            formed += 1
        
        # Try to contract window from left
        while left <= right and formed == required_count:
            char_left = s[left]
            
            # Save smallest window
            if right - left + 1 < result[0]:
                result = (right - left + 1, left, right)
            
            # Remove leftmost character
            window_counts[char_left] -= 1
            if char_left in required and window_counts[char_left] < required[char_left]:
                formed -= 1
            
            left += 1
    
    return "" if result[0] == float('inf') else s[result[1]:result[2] + 1]


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("ab", "b", "b"),
    ]
    
    for s, t, expected in test_cases:
        result = min_window(s, t)
        status = "✓" if result == expected else "✗"
        print(f"{status} s='{s}', t='{t}' -> '{result}' (Expected: '{expected}')")

