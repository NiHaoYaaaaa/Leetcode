class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for c in coins:
            for x in range(c, amount+1):
                dp[x] = min(dp[x], dp[x-c] + 1)
        return dp[amount] if dp[amount] <= amount else -1