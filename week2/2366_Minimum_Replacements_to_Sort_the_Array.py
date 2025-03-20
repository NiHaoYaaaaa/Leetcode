import math

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        count = 0
        cur_max = nums[-1]
        n = len(nums)
        for i in range(n-2, -1, -1):
            if cur_max == 1:
                count += nums[i] - 1
                continue
            if nums[i] > cur_max:
                tmp = nums[i]
                j = math.floor(tmp / cur_max)
                while(math.ceil(tmp / j) > cur_max):
                    j += 1
                cur_max = math.floor(tmp / j)
                count += j-1
            else:
                cur_max = nums[i]
        return count
        