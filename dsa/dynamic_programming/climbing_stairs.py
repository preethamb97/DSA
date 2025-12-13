"""
Climbing Stairs - LeetCode #70
Frequency: 90% (Extremely common - DP introduction)

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Time Complexity: O(n)
Space Complexity: O(1) optimized, O(n) with memoization
"""

from typing import Dict


def climb_stairs_recursive(n: int) -> int:
    """
    Recursive (inefficient): O(2^n) time
    """
    if n <= 2:
        return n
    return climb_stairs_recursive(n - 1) + climb_stairs_recursive(n - 2)


def climb_stairs_memo(n: int, memo: Dict[int, int] = None) -> int:
    """
    Memoization: O(n) time, O(n) space
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 2:
        return n
    
    memo[n] = climb_stairs_memo(n - 1, memo) + climb_stairs_memo(n - 2, memo)
    return memo[n]


def climb_stairs_dp(n: int) -> int:
    """
    Bottom-up DP: O(n) time, O(n) space
    """
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


def climb_stairs_optimized(n: int) -> int:
    """
    Space-optimized: O(n) time, O(1) space
    """
    if n <= 2:
        return n
    
    prev2, prev1 = 1, 2
    
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    
    return prev1


# Test cases
if __name__ == "__main__":
    test_cases = [1, 2, 3, 4, 5, 10]
    
    for n in test_cases:
        result = climb_stairs_optimized(n)
        print(f"n={n} -> {result} ways")
        # n=1: 1, n=2: 2, n=3: 3, n=4: 5, n=5: 8 (Fibonacci sequence)

