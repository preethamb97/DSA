"""
Edit Distance - LeetCode #72
Frequency: 75% (Very common - Microsoft favorite)

Given two strings word1 and word2, return the minimum number of operations 
required to convert word1 to word2 (insert, delete, replace).

Time Complexity: O(m * n)
Space Complexity: O(m * n) or O(min(m, n)) optimized
"""

from typing import List


def min_distance(word1: str, word2: str) -> int:
    """
    Bottom-up DP approach
    """
    m, n = len(word1), len(word2)
    
    # dp[i][j] = min operations to convert word1[:i] to word2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases
    for i in range(m + 1):
        dp[i][0] = i  # Delete all characters
    for j in range(n + 1):
        dp[0][j] = j  # Insert all characters
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                # Characters match, no operation needed
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Try all three operations
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # Delete
                    dp[i][j - 1],      # Insert
                    dp[i - 1][j - 1]   # Replace
                )
    
    return dp[m][n]


def min_distance_optimized(word1: str, word2: str) -> int:
    """
    Space-optimized: O(min(m, n)) space
    """
    m, n = len(word1), len(word2)
    
    # Use shorter string for DP array
    if m < n:
        word1, word2 = word2, word1
        m, n = n, m
    
    prev = list(range(n + 1))
    
    for i in range(1, m + 1):
        curr = [i] + [0] * n
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                curr[j] = prev[j - 1]
            else:
                curr[j] = 1 + min(prev[j], curr[j - 1], prev[j - 1])
        prev = curr
    
    return prev[n]


# Test cases
if __name__ == "__main__":
    test_cases = [
        ("horse", "ros", 3),      # horse -> rorse -> rose -> ros
        ("intention", "execution", 5),
        ("", "a", 1),
        ("a", "", 1),
    ]
    
    for word1, word2, expected in test_cases:
        result = min_distance(word1, word2)
        status = "✓" if result == expected else "✗"
        print(f"{status} '{word1}' -> '{word2}': {result} (Expected: {expected})")

