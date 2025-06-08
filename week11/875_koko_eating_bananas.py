import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        def finish(speed):
            return sum(math.ceil(p / speed) for p in piles) <= h

        while left < right:
            mid = (left + right) // 2
            if finish(mid):
                right = mid
            else:
                left = mid + 1

        return left