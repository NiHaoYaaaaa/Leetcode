class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1 / x
        negative = False
        if n < 0:
            negative = True
            n = abs(n)
        now = x
        ans = 1
        while n > 0:
            if n % 2 != 0:
                ans *= now
            now *= now
            n //= 2
        return ans if not negative else 1 / ans