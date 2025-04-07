class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(current, remaining):
            if not remaining:
                ans.append(current)
                return
            for i in range(len(remaining)):
                backtrack(current + [remaining[i]], remaining[:i] + remaining[i+1:])
        
        backtrack([], nums)
        return ans