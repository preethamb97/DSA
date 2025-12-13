"""
Coin Change - LeetCode #322
Frequency: 85% (Extremely common)

You are given an integer array coins representing coins of different denominations 
and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount.

Time Complexity: O(amount * len(coins))
Space Complexity: O(amount)
"""

from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    """
    Bottom-up DP approach
    """
    # dp[i] = minimum coins needed for amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1


def coin_change_memo(coins: List[int], amount: int) -> int:
    """
    Top-down memoization approach
    """
    memo = {}
    
    def dfs(remaining: int) -> int:
        if remaining == 0:
            return 0
        if remaining < 0:
            return float('inf')
        if remaining in memo:
            return memo[remaining]
        
        min_coins = float('inf')
        for coin in coins:
            result = dfs(remaining - coin)
            if result != float('inf'):
                min_coins = min(min_coins, result + 1)
        
        memo[remaining] = min_coins
        return min_coins
    
    result = dfs(amount)
    return result if result != float('inf') else -1


def coin_change_2(coins: List[int], amount: int) -> int:
    """
    Coin Change 2 - LeetCode #518
    Return the number of combinations that make up that amount
    """
    dp = [0] * (amount + 1)
    dp[0] = 1
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    
    return dp[amount]


# Test cases
if __name__ == "__main__":
    # Test Coin Change
    coins1 = [1, 2, 5]
    amount1 = 11
    result1 = coin_change(coins1, amount1)
    print(f"Coins: {coins1}, Amount: {amount1}")
    print(f"Minimum coins: {result1}")  # Expected: 3 (5 + 5 + 1)
    
    # Test Coin Change 2
    coins2 = [1, 2, 5]
    amount2 = 5
    result2 = coin_change_2(coins2, amount2)
    print(f"\nCoins: {coins2}, Amount: {amount2}")
    print(f"Number of combinations: {result2}")  # Expected: 4

