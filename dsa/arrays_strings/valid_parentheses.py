"""
Valid Parentheses - LeetCode #20
Frequency: 95% (Universal question)

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


def is_valid(s: str) -> bool:
    """
    Stack-based approach
    """
    if len(s) % 2 != 0:
        return False
    
    stack: List[str] = []
    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    for char in s:
        if char in mapping:
            # Closing bracket
            if not stack or stack.pop() != mapping[char]:
                return False
        else:
            # Opening bracket
            stack.append(char)
    
    return len(stack) == 0


def is_valid_optimized(s: str) -> bool:
    """
    Optimized version with early exit
    """
    stack: List[str] = []
    pairs = {'(': ')', '{': '}', '[': ']'}
    
    for char in s:
        if char in pairs:
            stack.append(char)
        elif not stack or pairs[stack.pop()] != char:
            return False
    
    return not stack


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(((", False),
    ]
    
    for s, expected in test_cases:
        result = is_valid(s)
        status = "✓" if result == expected else "✗"
        print(f"{status} Input: '{s}' -> {result} (Expected: {expected})")

