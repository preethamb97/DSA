"""
Longest Palindromic Substring - LeetCode #5
Frequency: 80% (Very common)

Given a string s, return the longest palindromic substring in s.

Time Complexity: O(n²) expand around centers, O(n) Manacher's algorithm
Space Complexity: O(1) expand, O(n) Manacher's
"""

from typing import Tuple


def longest_palindrome_expand(s: str) -> str:
    """
    Expand around centers: O(n²) time, O(1) space
    """
    if not s:
        return ""
    
    start = 0
    max_len = 1
    
    def expand_around_center(left: int, right: int) -> Tuple[int, int]:
        """Expand and return (start, length) of palindrome"""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - left - 1
    
    for i in range(len(s)):
        # Odd length palindromes (center at i)
        left, length = expand_around_center(i, i)
        if length > max_len:
            max_len = length
            start = left
        
        # Even length palindromes (center between i and i+1)
        left, length = expand_around_center(i, i + 1)
        if length > max_len:
            max_len = length
            start = left
    
    return s[start:start + max_len]


def longest_palindrome_dp(s: str) -> str:
    """
    DP approach: O(n²) time, O(n²) space
    """
    if not s:
        return ""
    
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start = 0
    max_len = 1
    
    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = True
    
    # Check for palindromes of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_len = 2
    
    # Check for palindromes of length 3 and more
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_len = length
    
    return s[start:start + max_len]


def count_substrings(s: str) -> int:
    """
    Palindromic Substrings - LeetCode #647
    Count total number of palindromic substrings
    """
    count = 0
    
    def expand_around_center(left: int, right: int) -> int:
        """Count palindromes expanding from center"""
        palindromes = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes += 1
            left -= 1
            right += 1
        return palindromes
    
    for i in range(len(s)):
        # Odd length
        count += expand_around_center(i, i)
        # Even length
        count += expand_around_center(i, i + 1)
    
    return count


# Test cases
if __name__ == "__main__":
    test_cases = [
        "babad",  # "bab" or "aba"
        "cbbd",   # "bb"
        "a",      # "a"
        "ac",     # "a" or "c"
    ]
    
    print("=== Longest Palindromic Substring ===")
    for s in test_cases:
        result1 = longest_palindrome_expand(s)
        result2 = longest_palindrome_dp(s)
        print(f"'{s}' -> Expand: '{result1}', DP: '{result2}'")
    
    # Test count substrings
    s = "abc"
    count = count_substrings(s)
    print(f"\nPalindromic substrings in '{s}': {count}")  # 3: "a", "b", "c"

