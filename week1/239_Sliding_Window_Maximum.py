from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        # k is 1
        if k == 1:
            return nums
        # k is 2
        if k == 2:
            for i in range(1, len(nums)):
                if nums[i] > nums[i-1]:
                    ans.append(nums[i])
                else:
                    ans.append(nums[i-1])
            return ans
        # if k >= 3
        dq = deque()
        dq.append(0)
        for i in range(1, k):
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
        ans.append(nums[dq[0]])
        for i in range(k, len(nums)):
            if dq[0] < i-k+1:
                dq.popleft()
            while dq and nums[i] > nums[dq[-1]]:
                dq.pop()
            dq.append(i)
            ans.append(nums[dq[0]])
        return ans
        