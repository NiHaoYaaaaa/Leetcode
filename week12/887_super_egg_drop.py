class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [0] * (k + 1)
        m = 0
        while dp[k] < n:
            m += 1
            for i in range(k, 0, -1):
                dp[i] = dp[i] + dp[i - 1] + 1
        return m