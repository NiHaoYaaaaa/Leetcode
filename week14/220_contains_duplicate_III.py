from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False 

        window = SortedList()

        for i in range(len(nums)):
            idx = window.bisect_left(nums[i] - valueDiff)
            if idx < len(window) and abs(window[idx] - nums[i]) <= valueDiff:
                return True

            window.add(nums[i])

            if len(window) > indexDiff:
                window.remove(nums[i - indexDiff])

        return False