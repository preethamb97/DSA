"""
Group Anagrams - LeetCode #49
Frequency: 80% (Very common)

Given an array of strings strs, group the anagrams together.

Time Complexity: O(n * k log k) where n is strings, k is max length
Space Complexity: O(n * k)
"""

from typing import List, Dict
from collections import defaultdict


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """
    Sort each string and use as key
    """
    groups: Dict[str, List[str]] = defaultdict(list)
    
    for s in strs:
        # Sort string to create key
        key = ''.join(sorted(s))
        groups[key].append(s)
    
    return list(groups.values())


def group_anagrams_count(strs: List[str]) -> List[List[str]]:
    """
    Use character count as key (more efficient for long strings)
    """
    groups: Dict[str, List[str]] = defaultdict(list)
    
    for s in strs:
        # Count characters
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        
        # Use tuple as key
        key = tuple(count)
        groups[key].append(s)
    
    return list(groups.values())


# Test cases
if __name__ == "__main__":
    test_cases = [
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [""],
        ["a"],
    ]
    
    for strs in test_cases:
        result = group_anagrams(strs)
        print(f"Input: {strs}")
        print(f"Output: {result}")
        print()

