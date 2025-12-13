"""
Longest Substring Without Repeating Characters - LeetCode #3
Frequency: 95% (Universal question)

Given a string s, find the length of the longest substring without repeating characters.

Time Complexity: O(n)
Space Complexity: O(min(n, m)) where m is the charset size
"""

from typing import Dict


def length_of_longest_substring(s: str) -> int:
    """
    Sliding window with hash map
    """
    if not s:
        return 0
    
    char_map: Dict[str, int] = {}
    max_length = 0
    start = 0
    
    for end in range(len(s)):
        # If character is seen and is within current window
        if s[end] in char_map and char_map[s[end]] >= start:
            start = char_map[s[end]] + 1
        
        char_map[s[end]] = end
        max_length = max(max_length, end - start + 1)
    
    return max_length


def length_of_longest_substring_set(s: str) -> int:
    """
    Sliding window with set (alternative approach)
    """
    if not s:
        return 0
    
    char_set = set()
    max_length = 0
    left = 0
    
    for right in range(len(s)):
        # Shrink window until no duplicates
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("abcabcbb", 3),  # "abc"
        ("bbbbb", 1),     # "b"
        ("pwwkew", 3),    # "wke"
        ("", 0),
        (" ", 1),
        ("dvdf", 3),      # "vdf"
    ]
    
    for s, expected in test_cases:
        result = length_of_longest_substring(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: '{s}' -> {result} (Expected: {expected})")

